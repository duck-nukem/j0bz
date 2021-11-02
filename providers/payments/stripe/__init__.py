from typing import Optional, List

import stripe
from stripe import Customer
from stripe.api_resources.checkout import Session

from domain.entities.job import Job
from domain.entities.user import Employer, User
from providers.payments.stripe.config import API_KEY, PAYMENT_SUCCESS_URL, PAYMENT_CANCEL_URL
from providers.payments.stripe.exceptions import StripeUserWithEmailAlreadyExistsException
from providers.payments.stripe.models import StripePaymentPlan, StripeSubscription

stripe.api_key = API_KEY


def list_active_payment_plans(limit=10) -> List[StripePaymentPlan]:
    return stripe.Price.list(limit=limit, active=True)['data']


def get_customer_by_email(email_address: str) -> Optional[Customer]:
    customer = stripe.Customer.list(email=email_address, limit=1)

    if customer.is_empty:
        return None

    return customer


def create_customer(user: User) -> str:
    existing_customer = get_customer_by_email(user.email_address)

    if existing_customer is not None:
        raise StripeUserWithEmailAlreadyExistsException

    customer = stripe.Customer.create(email=user.email_address, name=user.name)

    return customer['id']


def prepare_payment(
        job: Job,
        payer: Employer,
        products: List[StripeSubscription],
) -> Session:
    customer = get_customer_by_email(payer.email_address)
    subscription_payment = stripe.checkout.Session.create(
        line_items=[p.as_dict() for p in products],
        payment_method_types=['card'],
        mode='subscription',
        customer=customer['id'],
        client_reference_id=job.unique_id,
        success_url=PAYMENT_SUCCESS_URL,
        cancel_url=PAYMENT_CANCEL_URL,
    )

    return subscription_payment
