from domain.payments.actions import link_customer_payment_details
from domain.users.entities import User
from domain.users.repositories import UserRepository
from providers.payments.stripe import create_payment_account

user_repository = UserRepository()


def create_user(user: User):
    user = user_repository.create(user)
    payment_user_id = create_payment_account(user)
    link_customer_payment_details(user, payment_user_id)


def view_user(user_id) -> User:
    return user_repository.get(user_id)