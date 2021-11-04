from typing import TypeGuard, Any

from domain.jobs.exceptions import UnauthorizedPostException, AuthorIsNotOPException
from domain.users.entities import Employer


def assert_author_is_employer(poster: Any) -> TypeGuard[Employer]:
    if not isinstance(poster, Employer):
        raise UnauthorizedPostException

    return True


def assert_author_is_original_poster(author: Employer, original_poster: Employer):
    if author != original_poster:
        raise AuthorIsNotOPException
