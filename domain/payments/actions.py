from stripe.api_resources.checkout import Session

from domain.jobs.entities import Job
from domain.users.entities import Employer, User
from providers.databases import GenericDAO
from providers.databases.postgres.models import StripeUser
from providers.databases.postgres.models.job import JobPayment
from providers.payments.stripe import prepare_payment, StripeSubscription

payments = GenericDAO(JobPayment)
customers = GenericDAO(StripeUser)


def link_customer_payment_details(user: User, payment_user_id: str) -> None:
    customers.create({'stripe_customer_id': payment_user_id, 'user_id': user.id})


def link_job_payment_details(job: Job, payment: Session) -> None:
    payments.create({'job_id': job.id, 'payment_id': payment['id']})


def register_payment_intent(
        job: Job,
        payer: Employer,
        product: StripeSubscription,
):
    stripe_customer_id = customers.get_one(user_id=payer.id).stripe_customer_id
    payment = prepare_payment(job, stripe_customer_id, products=[product])
    link_job_payment_details(job, payment)
