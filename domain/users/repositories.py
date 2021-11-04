from typing import Dict

from sqlalchemy import select

from domain.users.entities import User
from providers.repositories import Repository
from providers.databases import GenericDAO
from providers.databases.postgres.connection import connect
from providers.databases.postgres.models.user import User as UserModel


class UserRepository(Repository):
    def __init__(self) -> None:
        self.dao = GenericDAO(UserModel)

    def to_db(self, user: User) -> Dict:
        user_dict = user.__dict__

        if 'id' in user_dict.keys() and user_dict['id'] is None:
            del user_dict['id']

        return user_dict

    def from_db(self, database_instance):
        instance_dict = {
            'name': database_instance.name,
            'username': database_instance.username,
            'email_address': database_instance.email_address,
            'type': database_instance.type,
            'id': database_instance.id,
        }
        return User(**instance_dict)

    def get_by_username(self, username: str) -> User:
        with connect() as db:
            query = select(UserModel).filter_by(username=username)
            results = db.execute(query)
            (result,) = results.one()

            return self.from_db(result)
