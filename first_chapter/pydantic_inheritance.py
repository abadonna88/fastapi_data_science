from datetime import date
from typing import List

from pydantic import BaseModel, validator, EmailStr, ValidationError, root_validator


class PostBase(BaseModel):
    title: str
    content: str
    
    def excerpt(self) -> str:
        return f"{self.content[:140]}..."


class PostCreate(PostBase):
    pass


class PostPublic(PostBase):
    id: int


class PostDB(PostBase):
    id: int
    nb_views: int = 0


class Person(BaseModel):
    first_name: str
    last_name: str
    birthdate: date
    
    @validator("birthdate")
    def valid_birthday(cls, v: date):
        delta = date.today() - v
        age = delta.days / 365
        if age > 120:
            raise ValueError("You seem a bit too old!")
        return v 


class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    password_confirmation: str
    
    @root_validator()
    def passwords_match(cls, values):
        password = values.get("password")
        password_confirmation = values.get("password_confirmation")
        if password != password_confirmation:
            raise ValueError("Passwords don't match")
        return values


class Model(BaseModel):
    values: List[int]
    
    @validator("values", pre=True)
    def split_string_values(cls, v):
        if isinstance(v, str):
            return v.split(",")
        return v 

