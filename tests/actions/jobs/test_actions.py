import unittest
from unittest import TestCase
from unittest.mock import patch

from domain.actions.jobs import post_job, update_job, delete_job, view_job, list_jobs
from tests.factories import JobFactory, EmployerFactory

MODULE_PATH = 'domain.actions.jobs'


class TestActions(TestCase):

    @patch(f'{MODULE_PATH}.JobRepository')
    @patch(f'{MODULE_PATH}.assert_author_is_employer')
    def test_post_job(
            self,
            patched_author_is_employer_assertion,
            patched_job_repository,
    ):
        job = JobFactory()
        employer = EmployerFactory()

        post_job(job, author=employer)

        patched_author_is_employer_assertion.assert_called_once()
        patched_job_repository().save.assert_called_once_with(job)

    @patch(f'{MODULE_PATH}.JobRepository')
    def test_view_job(self, patched_job_repository):
        job = JobFactory()

        view_job(job)

        patched_job_repository().get_by_id.assert_called_once_with(job.unique_id)

    @patch(f'{MODULE_PATH}.JobRepository')
    def test_list_jobs(self, patched_job_repository):
        list_jobs()

        patched_job_repository().get_all.assert_called_once()

    @patch(f'{MODULE_PATH}.JobRepository')
    @patch(f'{MODULE_PATH}.assert_author_is_employer')
    @patch(f'{MODULE_PATH}.assert_author_is_original_poster')
    def test_update_job(
            self,
            patched_author_is_op_assertion,
            patched_author_is_employer_assertion,
            patched_job_repository,
    ):
        employer = EmployerFactory()
        job = JobFactory(author=employer)
        updated_title = 'CEO'

        update_job(job, {'title': updated_title}, author=employer)

        patched_author_is_op_assertion.assert_called_once()
        patched_author_is_employer_assertion.assert_called_once()
        saved_job = patched_job_repository().save.mock_calls[0].args[0]
        self.assertEqual(saved_job.title, updated_title)

    @patch(f'{MODULE_PATH}.JobRepository')
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


if __name__ == '__main__':
    unittest.main()
