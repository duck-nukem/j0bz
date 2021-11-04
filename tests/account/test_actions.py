import unittest
from unittest import TestCase
from unittest.mock import patch

from domain.users.actions import create_user
from domain.users.entities import Candidate
from domain.users.repositories import UserRepository
from tests.factories import CandidateFactory


class TestUserActions(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user_repository = UserRepository()

    @patch('domain.users.actions.create_payment_account')
    def test_user_creation(self, patched_create_customer):
        user: Candidate = CandidateFactory()
        patched_create_customer.return_value = 'cus_ID'

        create_user(user)

        saved_user = self.user_repository.get_by_username(user.username)
        self.assertEqual(
            saved_user.username,
            user.username,
        )


if __name__ == '__main__':
    unittest.main()
