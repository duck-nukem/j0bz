from providers.payments.exceptions import PaymentProviderException


class StripeException(PaymentProviderException):
    pass


class StripeUserWithEmailAlreadyExistsException(StripeException):
    pass


class StripeUserWithEmailNotFoundException(StripeException):
    pass
