from typing import Dict

from dealer.models import DealerCar
from trades.models import Balance


def process_customer_order(validated_data: Dict):
    customer_id = validated_data['customer']
    car_id = validated_data['car']
    desired_amount = validated_data['amount']
    desired_price = validated_data['price'] / desired_amount
    dealers = DealerCar.objects.select_related('dealer').filter(price__lte=desired_price,
                                                                amount__gte=desired_amount) & DealerCar.objects.select_related(
        'car').filter(car_id=car_id).order_by('price')

    for dealer in dealers:
        print(dealer['amount'])
        dealer['amount'] -= desired_amount
        print(dealer['amount'])
        dealer_balances = Balance.objects.only('amount').filter(dealer_id=dealer.id).values()
        for dealer_balance in dealer_balances:
            dealer_balance['amount'] += dealer['price'] * desired_amount

        customer_balances = Balance.objects.only('amount').filter(customer_id=customer_id).values()
        for customer_balance in customer_balances:
            customer_balance['amount'] -= dealer['price'] * desired_amount

        customer_balance.save()
        dealer.save()


def check_customer_order(attrs: Dict) -> bool:
    customer_id = attrs['customer']
    balances = Balance.objects.only('amount').filter(customer_id=customer_id).values()
    customer_balance = .0
    for balance in balances:
        customer_balance = balance['amount']
    price = attrs['price']
    process_customer_order(attrs)
    return True if customer_balance > price else False
