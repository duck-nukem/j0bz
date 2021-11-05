from typing import Dict

from domain.jobs.entities import Job, Salary, Interview
from providers.repositories import Repository
from domain.users.repositories import UserRepository
from providers.databases import GenericDAO
from providers.databases.postgres.models.job import Job as JobModel

LIST_SEPARATOR = ','


class JobRepository(Repository):
    def __init__(self) -> None:
        self.dao = GenericDAO(db_model_class=JobModel)

    def to_db(self, job: Job) -> Dict:
        job_dict = {
            'author': job.author.id,
            'title': job.title,
            'location': job.location,
            'job_description': job.job_description,
            'status': job.status,
            'salary_min': job.salary.min,
            'salary_max': job.salary.max,
            'salary_currency_code': job.salary.currency_code,
            'interview_rounds': job.interview.rounds,
            'interview_description': job.interview.description,
            'benefits': LIST_SEPARATOR.join([b.value for b in job.benefits]),
            'posted_at': job.posted_at,
        }

        if job.id:
            job_dict['id'] = job.id

        return job_dict

    def from_db(self, job_instance: JobModel) -> Job:
        salary = Salary(
            min=job_instance.salary_min,
            max=job_instance.salary_max,
            currency_code=job_instance.salary_currency_code,
        )
        interview = Interview(
            rounds=job_instance.interview_rounds,
            description=job_instance.interview_description,
        )
        benefits = job_instance.benefits.split(LIST_SEPARATOR) \
            if LIST_SEPARATOR in job_instance.benefits \
            else []
        job_dict = {
            'id': job_instance.id,
            'author': UserRepository().get(job_instance.author),
            'title': job_instance.title,
            'location': job_instance.location,
            'job_description': job_instance.job_description,
            'salary': salary,
            'status': job_instance.status,
            'interview': interview,
            'benefits': benefits,
            'posted_at': job_instance.posted_at,
        }
        return Job(**job_dict)
