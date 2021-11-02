from stripe.api_resources.checkout import Session

from domain.entities.job import Job
from domain.entities.user import Employer
from providers.payments.stripe import prepare_payment, StripeSubscription

PRODUCT_PRICE_ID = 'price_1Jr64YBrjtXa4dr1dWRZ8Jcn'


def set_job_payment_id(job: Job, payment: Session) -> None:
    payment_id = payment['id']
    payment_status = payment['payment_status']  # unpaid/paid
    subscription_id = payment['subscription']  # None initially, id once paid
    # Webhook?


def generate_payment_url(
        job: Job,
        payer: Employer,
        product: StripeSubscription,
) -> str:
    payment = prepare_payment(job, payer, products=[product])
    set_job_payment_id(job, payment)

    return payment['url']
