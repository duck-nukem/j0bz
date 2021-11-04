import unittest
from unittest import TestCase
from unittest.mock import patch, sentinel

from domain.jobs.repositories import JobRepository
from domain.payments.actions import link_customer_payment_details, link_job_payment_details, register_payment_intent
from domain.users.repositories import UserRepository
from providers.databases import GenericDAO
from providers.databases.postgres.models import StripeUser
from providers.databases.postgres.models.job import JobPayment
from tests.factories import UserFactory, JobFactory


class TestPaymentActions(TestCase):
    def setUp(self) -> None:
        user_repository = UserRepository()
        self.user = user_repository.create(UserFactory())
        self.job_repository = JobRepository()
        super().setUp()

    def test_link_customer_payment_details(self):
        payment_id = 'cs_SAMPLE_ID'

        link_customer_payment_details(self.user, payment_id)

        stripe_dao = GenericDAO(StripeUser)
        payment_details = stripe_dao.get_one(user_id=self.user.id)
        self.assertEqual(payment_details.stripe_customer_id, payment_id)

    def test_link_job_payment_details(self):
        job = self.job_repository.create(JobFactory(author=self.user))
        mock_payment = {'id': 'cs_SAMPLE_ID'}

        # noinspection PyTypeChecker
        link_job_payment_details(job, mock_payment)

        job_payment_dao = GenericDAO(JobPayment)
        job_payment = job_payment_dao.get_one(job_id=job.id)
        self.assertEqual(job_payment.payment_id, mock_payment['id'])

    @patch('domain.payments.actions.prepare_payment')
    def test_register_payment_intent(self, patched_prepare_payment):
        payment_id = 'cs_SAMPLE_ID'
        patched_prepare_payment.return_value = {'id': payment_id}
        link_customer_payment_details(self.user, payment_id)
        job = self.job_repository.create(JobFactory(author=self.user))

        register_payment_intent(job, payer=self.user, product=sentinel.PRODUCT)

        patched_prepare_payment.assert_called_once_with(job, payment_id, products=[sentinel.PRODUCT])


if __name__ == '__main__':
    unittest.main()
