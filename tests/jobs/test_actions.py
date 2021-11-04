import unittest
from unittest import TestCase, skip
from unittest.mock import patch

from domain.jobs.actions import update_job, delete_job, view_job, list_jobs, post_job
from domain.jobs.entities import Job
from domain.jobs.repositories import JobRepository
from domain.payments.actions import link_customer_payment_details
from domain.users.repositories import UserRepository
from tests.factories import JobFactory, EmployerFactory

MODULE_PATH = 'domain.jobs.actions'


class TestActions(TestCase):
    def setUp(self) -> None:
        self.user_repository = UserRepository()
        self.job_repository = JobRepository()
        super().setUp()

    @patch(f'{MODULE_PATH}.assert_author_is_employer')
    @patch(f'{MODULE_PATH}.register_payment_intent')
    def test_post_job(
            self,
            patched_payment_url_generator,
            patched_author_is_employer_assertion,
    ):
        patched_payment_url_generator.return_value = 'https://example.com'
        job = self.simulate_user_post(JobFactory())

        patched_author_is_employer_assertion.assert_called_once()
        saved_job = self.job_repository.get(job.id)
        self.assertEqual(job.title, saved_job.title)

    @patch(f'{MODULE_PATH}.register_payment_intent')
    def test_view_job(self, patched_generate_payment_url):
        patched_generate_payment_url.return_value = 'https://example.com'
        job = JobFactory()
        self.simulate_user_post(job)

        result = view_job(job)

        self.assertEqual(result.title, job.title)

    @skip('Not implemented')
    @patch(f'{MODULE_PATH}.JobRepository')
    def test_list_jobs(self, patched_job_repository):
        list_jobs()

        patched_job_repository().get_all.assert_called_once()

    @patch(f'{MODULE_PATH}.register_payment_intent')
    @patch(f'{MODULE_PATH}.assert_author_is_employer')
    @patch(f'{MODULE_PATH}.assert_author_is_original_poster')
    def test_update_job(
            self,
            patched_author_is_op_assertion,
            patched_author_is_employer_assertion,
            patched_generate_payment_url,
    ):
        patched_generate_payment_url.return_value = 'https://example.com'
        job = JobFactory()
        self.simulate_user_post(job)
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

    def simulate_user_post(self, job: Job) -> Job:
        job_author = EmployerFactory()
        self.user_repository.create(job_author)
        link_customer_payment_details(job_author, 'cus_SAMPLE')

        return post_job(job, author=job_author)


if __name__ == '__main__':
    unittest.main()
