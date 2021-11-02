import unittest
from decimal import Decimal

from providers.payments.stripe.models import StripePaymentPlan


class TestStripePaymentPlan(unittest.TestCase):
    def test_parse_subscription_plan(self):
        mock_subscription = {
            'id': 'price_ID',
            'currency': 'usd',
            'product': 'prod_ID',
            'recurring': {
                'interval': 'week',
                'interval_count': 2,
                'trial_period_days': None,
            },
            'type': 'recurring',
            'unit_amount_decimal': '9900',
        }

        payment_plan = StripePaymentPlan(mock_subscription)

        expected_dict = {
            'currency': 'usd',
            'price': Decimal('99.00'),
            'recurrence': {
                'interval': 'week',
                'interval_count': 2,
                'trial_period_days': None,
            },
            'type': 'recurring',
        }
        self.assertDictEqual(payment_plan.as_dict(), expected_dict)

    def test_parse_one_time_payment(self):
        mock_one_time_payment = {
            'id': 'price_ID',
            'currency': 'usd',
            'product': 'prod_ID',
            'recurring': None,
            'type': 'one_time',
            'unit_amount_decimal': '9900',
        }

        payment_plan = StripePaymentPlan(mock_one_time_payment)

        expected_dict = {
            'currency': 'usd',
            'price': Decimal('99.00'),
            'recurrence': None,
            'type': 'one_time',
        }
        self.assertDictEqual(payment_plan.as_dict(), expected_dict)


if __name__ == '__main__':
    unittest.main()
