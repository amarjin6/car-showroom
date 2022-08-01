from typing import Dict

from orders.models import CustomerOrder
from dealer.models import DealerCar
from trades.models import Balance


def process_customer_order(order: CustomerOrder):
    desired_car = order.objects.select_related('car').all()
    desired_price = order.objects.only('price')
    desired_amount = order.objects.only('amount')
    dealers = DealerCar.objects.select_related('dealer').filter(price__lte=desired_price,
                                                                amount__lte=desired_amount) & DealerCar.objects.select_related(
        'car').filter(car=desired_car)

    print(dealers)


def check_customer_order(attrs: Dict) -> bool:
    customer_id = attrs['customer']
    balances = Balance.objects.only('amount').filter(customer_id=customer_id).values()
    for balance in balances:
        customer_balance = balance['amount']
    price = attrs['price']
    return True if customer_balance > price else False
