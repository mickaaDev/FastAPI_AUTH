import fastapi.security as _security
import fastapi as _fastapi
import database as _dt
import sqlalchemy.orm as _orm
import schemas as _schemas
import models as _models
import email_validator as _email_check
import passlib.hash as _hash
import jwt as _jwt


_JWT_SECRET = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"

oauth2schema = _security.OAuth2PasswordBearer("/api/token")


def create_database():
    return _dt.Base.metadata.create_all(bind=_dt.engine)


def get_db():
    db = _dt.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_user_by_email(email: str, db: _orm.Session):
    return db.query(_models.User).filter(_models.User.email == email).first()


async def create_user(user: _schemas.UserCreate, db: _orm.Session):
    try:
        valid = _email_check.validate_email(email=user.email)
        email = valid.email
    except _email_check.EmailNotValidError:
        raise _fastapi.HTTPException(
            status_code=400, detail="Please enter a valid email!"
        )

    hashed_password = _hash.bcrypt.hash(user.password)
    user_obj = _models.User(email=email, hashed_password=hashed_password)

    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj


async def create_token(user: _models.User):
    user_schema_obj = _schemas.User.from_orm(user)

    user_dict = user_schema_obj.dict()
    del user_dict['date_created']

    token = _jwt.encode(user_dict, _JWT_SECRET)

    return dict(access_token=token, token_type='bearer')


async def authenticate_user(email: str, password: str, db: _orm.Session):
    user = await  get_user_by_email(email=email, db=db)

    if not user:
        return False

    if not user.verify_password(password=password):
        return False
    return user


async def get_current_user(
        db: _orm.Session = _fastapi.Depends(get_db),
        token: str = _fastapi.Depends(oauth2schema), ):
    try:
        payload = _jwt.decode(token, _JWT_SECRET, algorithms=["HS256"])
        user = db.query(_models.User).get(payload["id"])
    except:
        raise _fastapi.HTTPException(
            status_code=401, detail='Invalid email or password'
        )
    return _schemas.User.from_orm(user)


async def create_image(user: _schemas.User, db: _orm.Session, image: _schemas.ImageCreate):
    image = _models.Image(**image.dict(), owner_id=user.id)
    db.add(image)
    db.commit()
    db.refresh(image)
    return _schemas.Image.from_orm(image)
