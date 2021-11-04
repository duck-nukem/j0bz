from typing import Dict, Any, Iterable

from domain.jobs.assertions import assert_author_is_employer, assert_author_is_original_poster
from domain.jobs.entities import Job, JobStatus
from domain.jobs.repositories import JobRepository
from domain.payments.actions import register_payment_intent
from domain.payments.assertions import assert_has_active_subscription
from domain.payments.exceptions import ActiveSubscriptionNotFoundException
from domain.users.entities import User
from providers.payments.stripe import StripeSubscription

# TODO: hard-coded for now, should come as an input
SUBSCRIPTION_PRICE_ID = 'price_1JrnUqBrjtXa4dr1LqmienET'
job_repository = JobRepository()


def post_job(job: Job, author: User) -> Job:
    assert_author_is_employer(author)

    job.author = author
    job.status = JobStatus.AWAITING_PAYMENT
    saved_job = job_repository.create(job)

    register_payment_intent(
        saved_job,
        payer=author,
        product=StripeSubscription(price_id=SUBSCRIPTION_PRICE_ID),
    )

    return saved_job


def view_job(job: Job) -> Job:
    return job_repository.get(job.id)


def list_jobs() -> Iterable[Job]:
    return job_repository.get_all()


def update_job(job: Job, update: Dict[str, Any], author: User):
    assert_author_is_employer(author)
    assert_author_is_original_poster(author, job.author)

    job_repository.update(job, update)


def delete_job(job: Job, author: User):
    assert_author_is_employer(author)
    assert_author_is_original_poster(author, job.author)

    job_repository.delete(job)


def update_job_payment_status(job: Job):
    try:
        assert_has_active_subscription(job.id)
    except ActiveSubscriptionNotFoundException:
        job.status = JobStatus.AWAITING_PAYMENT
    else:
        job.status = JobStatus.ACTIVE

    job_repository.update(job, {'status': job.status})
