import factory
from factory import SubFactory

from domain.entities.job import Job
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
