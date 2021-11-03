from domain.actions.payments import link_customer_payment_details
from domain.entities.user import User
from domain.repositories.user_repository import UserRepository
from providers.payments.stripe import create_payment_account

user_repository = UserRepository()


def create_user(user: User):
    user = user_repository.create(user)
    payment_user_id = create_payment_account(user)
    link_customer_payment_details(user, payment_user_id)
