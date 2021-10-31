from dataclasses import dataclass

from domain.entities import Entity


@dataclass
class User(Entity):
    name: str

    def __eq__(self, other):
        return self.name == other.name


@dataclass
class Employer(User):
    pass


@dataclass
class Candidate(User):
    pass
