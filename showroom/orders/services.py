from typing import Dict

from dealer.models import DealerCar
from trades.models import Balance
from users.models import UserProfile
from cars.models import Car


def process_customer_order(validated_data: Dict):
    customer_profile = UserProfile.objects.get(id=validated_data.get('customer'))
    car_profile = Car.objects.get(id=validated_data.get('car'))
    desired_amount = validated_data['amount']
    desired_price = validated_data['price'] / desired_amount
    dealers = DealerCar.objects.select_related('dealer').filter(price__lte=desired_price, amount__gte=desired_amount,
                                                                car__id=car_profile.id).order_by('price')

    dealer = dealers[0]

    final_price = dealer.price * desired_amount

    dealer_balance = dealer.dealer.profile.profile_balance.only('amount')
    dealer_balance[0].amount += final_price
    dealer.amount -= desired_amount

    customer_balance = customer_profile.profile_balance.only('amount')
    customer_balance[0].amount -= final_price

    dealer.save()
    dealer_balance[0].save()
    customer_balance[0].save()


def check_order(client_name: str, attrs: Dict) -> tuple:
    user_profile = UserProfile.objects.get(id=attrs.get(client_name).id)
    balances = user_profile.profile_balance.only('amount')
    client_balance = .0
    for balance in balances:
        client_balance = balance.amount

    price = attrs['price']

    return client_balance >= price
