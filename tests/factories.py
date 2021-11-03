from uuid import uuid4

import factory
from factory import SubFactory

from domain.entities.job import Job, Salary, Interview
from domain.entities.user import Employer, Candidate, User, UserType


class UserFactory(factory.Factory):
    class Meta:
        model = User

    name = factory.Faker('name')
    username = factory.Faker('email')
    email_address = factory.Faker('email')
    type = UserType.candidate


class CandidateFactory(UserFactory):
    class Meta:
        model = Candidate

    type = UserType.candidate


class EmployerFactory(UserFactory):
    class Meta:
        model = Employer

    name = factory.Faker('company')
    type = UserType.employer


class JobFactory(factory.Factory):
    class Meta:
        model = Job

    author = SubFactory(EmployerFactory)
    title = factory.Faker('job')
    location = 'GB'
    job_description = '## Markdown'
    salary = Salary(
        currency_code='USD',
        min=100,
    )
    interview = Interview(
        rounds=2,
    )
    benefits = []
