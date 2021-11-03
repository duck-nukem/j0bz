import unittest
from unittest import TestCase

from domain.actions.jobs.assertions import assert_author_is_employer, assert_author_is_original_poster
from domain.actions.jobs.exceptions import UnauthorizedPostException, AuthorIsNotOPException
from domain.repositories.user_repository import UserRepository
from tests.factories import EmployerFactory, JobFactory, CandidateFactory, UserFactory


class TestAuthorIsEmployerAssertion(TestCase):
    def setUp(self) -> None:
        self.user_repository = UserRepository()

    def test_unregistered_employer_cannot_post(self):
        unregistered_user = UserFactory()
        self.user_repository.create(unregistered_user)

        with self.assertRaises(UnauthorizedPostException):
            # noinspection PyTypeChecker
            assert_author_is_employer(unregistered_user)

    def test_candidate_cannot_post(self):
        candidate = CandidateFactory()
        self.user_repository.create(candidate)

        with self.assertRaises(UnauthorizedPostException):
            # noinspection PyTypeChecker
            assert_author_is_employer(poster=candidate)


class TestAuthorIsOriginalAuthor(TestCase):
    def setUp(self) -> None:
        self.user_repository = UserRepository()

    def test_any_employer_is_not_the_original_poster(self):
        any_employer = EmployerFactory()
        job = JobFactory()

        with self.assertRaises(AuthorIsNotOPException):
            # noinspection PyTypeChecker
            assert_author_is_original_poster(any_employer, job.author)

    def test_op_is_original_poster_does_not_raise_exception(self):
        original_poster = EmployerFactory()
        job = JobFactory(author=original_poster)

        assert_author_is_original_poster(original_poster, job.author)


if __name__ == '__main__':
    unittest.main()
