import unittest
from unittest import TestCase, skip
from unittest.mock import patch

from domain.jobs.actions import update_job, delete_job, view_job, list_jobs, post_job, update_job_payment_status
from domain.jobs.entities import Job, JobStatus
from domain.jobs.repositories import JobRepository
from domain.payments.actions import link_customer_payment_details
from domain.payments.exceptions import ActiveSubscriptionNotFoundException
from domain.users.repositories import UserRepository
from tests.factories import JobFactory, EmployerFactory

MODULE_PATH = 'domain.jobs.actions'


@patch(f'{MODULE_PATH}.register_payment_intent', return_value='http://t.co')
class TestActions(TestCase):
    def setUp(self) -> None:
        self.user_repository = UserRepository()
        self.job_repository = JobRepository()
        super().setUp()

    @patch(f'{MODULE_PATH}.assert_author_is_employer')
    def test_post_job(
            self,
            _patched_payment_url_generator,
            patched_author_is_employer_assertion,
    ):
        job = self._simulate_user_post(JobFactory())

        patched_author_is_employer_assertion.assert_called_once()
        saved_job = self.job_repository.get(job.id)
        self.assertEqual(job.title, saved_job.title)

    def test_view_job(self, _patched_generate_payment_url):
        job = JobFactory()
        self._simulate_user_post(job)

        result = view_job(job)

        self.assertEqual(result.title, job.title)

    @skip('Not implemented')
    @patch(f'{MODULE_PATH}.JobRepository')
    def test_list_jobs(self, patched_job_repository):
        list_jobs()

        patched_job_repository().get_all.assert_called_once()

    @patch(f'{MODULE_PATH}.assert_author_is_employer')
    @patch(f'{MODULE_PATH}.assert_author_is_original_poster')
    def test_update_job(
            self,
            patched_author_is_op_assertion,
            patched_author_is_employer_assertion,
            _patched_generate_payment_url,
    ):
        job = JobFactory()
        self._simulate_user_post(job)
        updated_title = 'CEO'
        patched_author_is_employer_assertion.reset_mock()
        patched_author_is_op_assertion.reset_mock()

        update_job(job, {'title': updated_title}, author=job.author)

        patched_author_is_op_assertion.assert_called_once()
        patched_author_is_employer_assertion.assert_called_once()
        saved_job = self.job_repository.get(job.id)
        self.assertEqual(saved_job.title, updated_title)

    @skip('Not implemented')
    @patch(f'{MODULE_PATH}.assert_author_is_employer')
    @patch(f'{MODULE_PATH}.assert_author_is_original_poster')
    def test_delete_job(
            self,
            patched_author_is_op_assertion,
            patched_author_is_employer_assertion,
            patched_job_repository,
    ):
        employer = EmployerFactory()
        job = JobFactory(author=employer)

        delete_job(job, author=employer)

        patched_author_is_op_assertion.assert_called_once()
        patched_author_is_employer_assertion.assert_called_once()
        patched_job_repository().delete.assert_called_once_with(job)

    @patch(f'{MODULE_PATH}.assert_has_active_subscription')
    def test_update_job_payment_status(
            self,
            patched_has_active_subscription,
            _patched_register_payment_intent,
    ):
        saved_job = self._simulate_user_post()

        update_job_payment_status(saved_job)

        patched_has_active_subscription.assert_called_once_with(saved_job.id)
        self.assertEqual(self.job_repository.get(saved_job.id).status, JobStatus.ACTIVE)

    @patch(f'{MODULE_PATH}.assert_has_active_subscription')
    def test_update_job_payment_status_without_sub(
            self,
            patched_has_active_subscription,
            _patched_register_payment_intent,
    ):
        patched_has_active_subscription.side_effect = ActiveSubscriptionNotFoundException
        saved_job = self._simulate_user_post()

        update_job_payment_status(saved_job)

        self.assertEqual(self.job_repository.get(saved_job.id).status, JobStatus.AWAITING_PAYMENT)

    def _simulate_user_post(self, job: Job = None) -> Job:
        if job is None:
            job = JobFactory()

        job_author = EmployerFactory()
        self.user_repository.create(job_author)
        link_customer_payment_details(job_author, 'cus_SAMPLE')

        return post_job(job, author=job_author)


if __name__ == '__main__':
    unittest.main()
