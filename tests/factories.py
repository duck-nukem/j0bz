import factory
from factory import SubFactory

from domain.entities.job import Job
from domain.entities.user import Employer


class EmployerFactory(factory.Factory):
    class Meta:
        model = Employer

    name = factory.Faker('company')


class JobFactory(factory.Factory):
    class Meta:
        model = Job

    author = SubFactory(EmployerFactory)
    title = factory.Faker('job')
