from datetime import date, datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, ValidationError, Field


class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"


class Address(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str


class Person(BaseModel):
    first_name: str = Field(..., min_length=3)
    last_name: str = Field(..., min_length=3)
    age: Optional[int] = Field(None, ge=0, le=120)
    gender: Gender
    birthdate: date
    interests: List[str]
    address: Address


class UserProfile(BaseModel):
    nickname: str
    location: Optional[str] = None
    subscribed_newsletter: bool = True


def list_factory():
    return ["a", "b", "c"]


class Model(BaseModel):
    l: List[str] = Field(default_factory=list_factory)
    d: datetime = Field(default_factory=datetime.now)
    l2: List[str] = Field(default_factory=list)

