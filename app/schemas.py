import datetime as _dt
import pydantic as _pydantic


class UserBase(_pydantic.BaseModel):
    email: str


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True


class ImageBase(_pydantic.BaseModel):
    image_text: str


class ImageCreate(ImageBase):
    pass


class Image(ImageBase):
    id: int
    owner_id: int
    date_created: _dt.datetime

    class Config:
        orm_mode = True
