from stripe.api_resources.checkout import Session

from domain.entities.job import Job
from domain.entities.user import Employer, User
from providers.databases import GenericDAO
from providers.databases.postgres.models import StripeUser
from providers.databases.postgres.models.job import JobPayment
from providers.payments.stripe import prepare_payment, StripeSubscription


def link_customer_payment_details(user: User, payment_user_id: str) -> None:
    stripe_dao = GenericDAO(StripeUser)
    stripe_dao.create({'stripe_customer_id': payment_user_id, 'user_id': user.id})


def link_job_payment_details(job: Job, payment: Session) -> None:
    job_payment_dao = GenericDAO(JobPayment)
    job_payment_dao.create({'job_id': job.id, 'payment_id': payment['id']})


def register_payment_intent(
        job: Job,
        payer: Employer,
        product: StripeSubscription,
):
    stripe_customer_dao = GenericDAO(StripeUser)
    stripe_customer_id = stripe_customer_dao.get_one(user_id=payer.id).stripe_customer_id
    payment = prepare_payment(job, stripe_customer_id, products=[product])
    link_job_payment_details(job, payment)
