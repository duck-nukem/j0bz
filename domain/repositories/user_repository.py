from sqlalchemy import select

from domain.entities.user import User
from providers.databases.postgres.connection import database
from providers.databases.postgres.models.user import User as UserModel, StripeUser


class UserRepository:
    async def create(self, user: User):
        user_model = UserModel(**user.__dict__)
        database.add(user_model)
        await database.commit()

    async def link_payment_details(self, user: User, payment_user_id: str) -> None:
        user = await self.get_by_username(user.username)
        stripe_user = StripeUser(stripe_customer_id=payment_user_id, user_id=user.id)

        database.add(stripe_user)
        await database.commit()

    async def get_by_username(self, username: str):
        query = select(UserModel).filter_by(username=username)
        results = await database.execute(query)
        (result,) = results.one()

        return result
