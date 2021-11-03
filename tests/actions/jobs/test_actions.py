import unittest
from unittest import TestCase, skip
from unittest.mock import patch

from domain.actions.jobs import update_job, delete_job, view_job, list_jobs, post_job
from domain.entities.job import Job
from domain.repositories.job_repository import JobRepository
from domain.repositories.user_repository import UserRepository
from tests.factories import JobFactory, EmployerFactory

MODULE_PATH = 'domain.actions.jobs'


class TestActions(TestCase):
    def setUp(self) -> None:
        self.user_repository = UserRepository()
        self.job_repository = JobRepository()
        super().setUp()

    @patch(f'{MODULE_PATH}.assert_author_is_employer')
    def test_post_job(
            self,
            patched_author_is_employer_assertion,
    ):
        job = JobFactory()
        self.simulate_user_post(job)

        patched_author_is_employer_assertion.assert_called_once()
        saved_job = self.job_repository.get(job.id)
        self.assertEqual(job.title, saved_job.title)

    def test_view_job(self):
        job = JobFactory()
        self.simulate_user_post(job)

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
    ):
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

    def simulate_user_post(self, job: Job):
        job_author = EmployerFactory()
        self.user_repository.create(job_author)
        post_job(job, author=job_author)


if __name__ == '__main__':
    unittest.main()
