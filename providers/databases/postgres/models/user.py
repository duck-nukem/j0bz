from sqlalchemy import Column, Integer, Enum, Unicode, String, ForeignKey

from domain.entities.user import UserType
from providers.databases.postgres import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(256), nullable=False)
    username = Column(String(64), nullable=False)
    email_address = Column(Unicode(256), nullable=False)
    type = Column(Enum(UserType), nullable=False)


class StripeUser(Base):
    __tablename__ = 'stripe_users'

    stripe_customer_id = Column(String(256), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
