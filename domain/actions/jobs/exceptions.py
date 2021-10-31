class JobPostException(Exception):
    pass


class UnauthorizedPostException(JobPostException):
    pass


class AuthorIsNotOPException(JobPostException):
    pass
