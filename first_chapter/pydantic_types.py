from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError


class User(BaseModel):
    email: EmailStr
    website: HttpUrl
