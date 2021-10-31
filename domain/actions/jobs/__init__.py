from typing import Dict, Any, Optional, Iterable

from domain.actions.jobs.assertions import assert_author_is_employer, assert_author_is_original_poster
from domain.entities.job import Job
from domain.entities.user import User
from domain.repositories.job_repository import JobRepository


def post_job(job: Job, author: User):
    assert_author_is_employer(author)

    JobRepository().save(job)


def view_job(job: Job, _author: Optional[User] = None) -> Job:
    return JobRepository().get_by_id(job.unique_id)


def list_jobs() -> Iterable[Job]:
    return JobRepository().get_all()


def update_job(job: Job, update: Dict[str, Any], author: User):
    assert_author_is_employer(author)
    assert_author_is_original_poster(author, job.author)

    job.update(update)

    JobRepository().save(job)


def delete_job(job: Job, author: User):
    assert_author_is_employer(author)
    assert_author_is_original_poster(author, job.author)

    JobRepository().delete(job)
