import unittest
from unittest import IsolatedAsyncioTestCase

from unittest.mock import patch

from domain.actions.account import create_user
from domain.entities.user import Candidate
from domain.repositories.user_repository import UserRepository
from tests.factories import CandidateFactory


class TestUserActions(IsolatedAsyncioTestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user_repository = UserRepository()

    @patch('domain.actions.account.create_customer')
    async def test_user_creation(self, patched_create_customer):
        user: Candidate = CandidateFactory()
        patched_create_customer.return_value = 'cus_ID'

        await create_user(user)

        saved_user = await self.user_repository.get_by_username(user.username)
        self.assertEqual(
            saved_user.username,
            user.username,
        )


if __name__ == '__main__':
    unittest.main()
