import json
import uuid

from django.conf import settings
from yookassa import Configuration, Payment


def create_payment(amount):
    Configuration.account_id = settings.SHOP_ID
    Configuration.secret_key = settings.YOOKASSA_API_KEY
    
    payment = Payment.create({
        'amount': {
            'value': amount,
            'currency': 'RUB'
        },
        'confirmation': {
            'type': 'redirect',
            'return_url': 'https://www.merchant-website.com/return_url'
        },
        'capture': True,
        'description': 'Оплата торта'
    }, uuid.uuid4())
    
    payment = json.loads(payment.json())
    
    return {
        'id': payment['id'],
        'url': payment['confirmation']['confirmation_url']
    }