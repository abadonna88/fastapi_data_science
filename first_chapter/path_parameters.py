from enum import Enum


class UserType(str, Enum):
    STANDARD = "standard"
    ADMIN = "admin"

