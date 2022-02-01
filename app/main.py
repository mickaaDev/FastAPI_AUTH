from fastapi import FastAPI
import fastapi as _fastapi
import fastapi.security as _security
import sqlalchemy.orm as _orm
import services as _services
import schemas as _schemas

apps = FastAPI()
_services.create_database()



@apps.get("/")
async def read_main():
    return {"msg": "Hello World"}


@apps.post("/api/users")
async def create_user(user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_user = await _services.get_user_by_email(email=user.email, db=db)
    if db_user:
        raise _fastapi.HTTPException(
            status_code=400, detail='User with that email already exists!'
        )
    user = await _services.create_user(user=user, db=db)

    return await _services.create_token(user=user)


@apps.post('/api/token')
async def generate_token(
        form_data: _security.OAuth2PasswordRequestForm = _fastapi.Depends(), db: _orm.Session =
        _fastapi.Depends(_services.get_db)
):
    user = await _services.authenticate_user(
        email=form_data.username, password=form_data.password, db=db
    )

    if not user:
        raise _fastapi.HTTPException(status_code=401, detail='Invalid Credentials!')

    return await _services.create_token(user=user)


@apps.get("/api/users/me", response_model=_schemas.User)
async def get_user(user: _schemas.User = _fastapi.Depends(_services.get_current_user)):
    return user


@apps.post("/api/image", response_model=_schemas.Image)
async def create_image(
        image: _schemas.ImageCreate,
        user: _schemas.User = _fastapi.Depends(_services.get_current_user),
        db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    return await _services.create_image(user=user, db=db, image=image)







from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional
class Item(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
fake_secret_token = "coneofsilence"

fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}

@apps.post("/items/", response_model=Item)
async def create_item(item: Item, x_token: str = Header(...)):
    if x_token != fake_secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_db[item.id] = item
    return item
