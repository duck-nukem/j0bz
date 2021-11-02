from dataclasses import dataclass
from decimal import Decimal
from typing import Dict


class StripePaymentPlan:
    def __init__(self, response_json: Dict) -> None:
        price = Decimal(response_json['unit_amount_decimal']) / 100
        self.price = price.quantize(Decimal('.01'))
        self.currency = response_json['currency']
        self.recurrence = response_json['recurring']
        self.type = response_json['type']

    def as_dict(self):
        return {
            'currency': self.currency,
            'price': self.price,
            'recurrence': self.recurrence,
            'type': self.type,
        }


@dataclass
class StripeSubscription:
    price_id: str
    quantity: int = 1

    def as_dict(self):
        return {'price': self.price_id, 'quantity': self.quantity}
