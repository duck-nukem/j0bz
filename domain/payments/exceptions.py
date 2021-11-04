class PaymentException(Exception):
    pass


class ActiveSubscriptionNotFoundException(PaymentException):
    pass
