from dataclasses import dataclass
from enum import Enum


class UserType(Enum):
    employer = 'EMPLOYER'
    candidate = 'CANDIDATE'


@dataclass
class User:
    name: str
    username: str
    email_address: str
    type: UserType

    id: int | None = None


@dataclass
class Employer(User):
    type = UserType.employer


@dataclass
class Candidate(User):
    type = UserType.candidate
