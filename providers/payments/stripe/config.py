from os import environ

API_KEY = environ.get('STRIPE_API_KEY', None)
PAYMENT_SUCCESS_URL = 'http://google.com'
PAYMENT_CANCEL_URL = 'http://google.com'