from dataclasses import dataclass
from enum import Enum

from domain.entities import Entity


class UserType(Enum):
    employer = 'EMPLOYER'
    candidate = 'CANDIDATE'


@dataclass
class User(Entity):
    name: str
    username: str
    email_address: str
    type: UserType

    def __eq__(self, other):
        return self.name == other.name


@dataclass
class Employer(User):
    type = UserType.employer


@dataclass
class Candidate(User):
    type = UserType.candidate
