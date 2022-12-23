from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint

#Users
#Create User
class UserCreate(BaseModel):
    email: EmailStr
    password: str

#Response Schema
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode= True

#AuthenticateUser
class UserLogin(BaseModel):
    email: EmailStr
    password: str

#Token
class Token(BaseModel):
    access_token: str
    token_type: str

#Token Data
class TokenData(BaseModel):
    id:Optional[str] = None
    expires: Optional[datetime]

#Posts
#Request Schema
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

#Response Schema
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode= True


class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1)


class PostOut(BaseModel):
    Post: Post
    votes:int

    class Config:
        orm_mode = True