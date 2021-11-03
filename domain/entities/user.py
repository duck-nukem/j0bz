from dataclasses import dataclass
from enum import Enum


class UserType(Enum):
    EMPLOYER = 'employer'
    CANDIDATE = 'candidate'


@dataclass
class User:
    name: str
    username: str
    email_address: str
    type: UserType

    id: int | None = None


@dataclass
class Employer(User):
    type = UserType.EMPLOYER


@dataclass
class Candidate(User):
    type = UserType.CANDIDATE
