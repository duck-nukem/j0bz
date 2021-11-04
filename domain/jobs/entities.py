from dataclasses import dataclass
from enum import Enum
from typing import List

from domain.users.entities import Employer


class JobStatus(Enum):
    DRAFT = 'draft'
    ACTIVE = 'active'
    AWAITING_PAYMENT = 'awaiting_payment'
    PAYMENT_EXPIRED = 'expired'


class Benefit(Enum):
    FULL_REMOTE = 'FULL_REMOTE'
    FOUR_DAY_WORK_WEEK = '4DAYWEEK'
    SIX_WORKING_HOURS = '6HOURSDAY'


@dataclass
class Salary:
    currency_code: str
    min: float
    max: float | None = None

    @property
    def range(self):
        return self.min if self.max is None else f'{self.min} - {self.max}'


@dataclass
class Interview:
    rounds: int
    description: str | None = None


@dataclass
class Job:
    author: Employer
    benefits: List[Benefit]
    interview: Interview
    job_description: str
    location: str
    salary: Salary
    status: JobStatus
    title: str

    id: int | None = None
