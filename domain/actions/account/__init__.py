from domain.entities.user import User
from domain.repositories.user_repository import UserRepository
from providers.payments.stripe import create_customer


async def create_user(user: User):
    user_repository = UserRepository()
    await user_repository.create(user)
    payment_user_id = create_customer(user)
    await user_repository.link_payment_details(user, payment_user_id)
