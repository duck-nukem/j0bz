from domain.payments.actions import payments
from domain.payments.exceptions import ActiveSubscriptionNotFoundException
from providers.payments.stripe import get_payment_subscription_status, StripePaidSubscriptionNotFoundException


def assert_has_active_subscription(entity_id: int) -> str:
    payment_id = payments.get_one(job_id=entity_id).payment_id

    try:
        subscription_status = get_payment_subscription_status(payment_id)
    except StripePaidSubscriptionNotFoundException:
        raise ActiveSubscriptionNotFoundException

    if subscription_status not in ['active', 'trialing']:
        raise ActiveSubscriptionNotFoundException

    return subscription_status
