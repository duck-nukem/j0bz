from dataclasses import dataclass
from uuid import uuid4

from domain.entities import Entity
from domain.entities.user import Employer


@dataclass
class Job(Entity):
    readonly_field_names = ['unique_id']

    unique_id = uuid4()
    author: Employer
    title: str
