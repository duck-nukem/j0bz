from dataclasses import dataclass
from enum import Enum
from typing import List

from domain.entities.user import Employer


class Benefit(Enum):
    FULL_REMOTE = 'FULL_REMOTE'
    FOUR_DAY_WORK_WEEK = '4DAYWEEK'
    SIX_WORKING_HOURS = '6HOURSDAY'


@dataclass
class Salary:
    currency_code: str
    min: float
    max: float | None = None


@dataclass
class Interview:
    rounds: int
    description: str | None = None


@dataclass
class Job:
    author: Employer
    title: str
    location: str
    job_description: str
    salary: Salary
    interview: Interview
    benefits: List[Benefit]

    id: int | None = None
