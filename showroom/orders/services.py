from typing import Dict

from dealer.models import Dealer, DealerCar
from users.models import UserProfile, UserProfileCar
from cars.models import Car
from core.enums import Profile


def check_order(client_name: str, attrs: Dict) -> tuple:
    if client_name == Profile.CUSTOMER:
        user_profile = UserProfile.objects.get(id=attrs.get(client_name).id)
        balances = user_profile.profile_balance.only('amount')

    else:
        dealer_profile = Dealer.objects.get(id=attrs.get(client_name).id)
        balances = dealer_profile.profile.profile_balance.only('amount')

    client_balance = .0
    for balance in balances:
        client_balance = balance.amount

    price = attrs['price']

    return client_balance >= price


def process_customer_order(order: Dict):
    customer_profile = UserProfile.objects.get(id=order.get('customer'))
    car_profile = Car.objects.get(id=order.get('car'))
    desired_amount = order['amount']
    desired_price = order['price'] / desired_amount
    dealers = DealerCar.objects.select_related('dealer').filter(price__lte=desired_price,
                                                                amount__gte=desired_amount,
                                                                car__id=car_profile.id).order_by('price')

    if dealers:
        dealer = dealers[0]

        final_price = dealer.price * desired_amount

        dealer_balances = dealer.dealer.profile.profile_balance.only('amount')
        if dealer_balances:
            dealer_balance = dealer_balances[0]
            dealer_balance.amount += final_price
            dealer.amount -= desired_amount
            dealer_balance.save()

        customer_balances = customer_profile.profile_balance.only('amount')
        if customer_balances:
            customer_balance = customer_balances[0]
            customer_balance.amount -= final_price
            customer_balance.save()

        dealer.save()


def process_dealer_order(order: Dict):
    dealer_profile = Dealer.objects.get(id=order.get('dealer'))
    car_profile = Car.objects.get(id=order.get('car'))
    desired_amount = order['amount']
    desired_price = order['price'] / desired_amount
    vendors = UserProfileCar.objects.select_related('profile').filter(price__lte=desired_price,
                                                                      amount__gte=desired_amount,
                                                                      car__id=car_profile.id).order_by('price')

    if vendors:
        vendor = vendors[0]

        final_price = vendor.price * desired_amount

        dealer_balances = dealer_profile.profile_balance.only('amount')
        if dealer_balances:
            dealer_balance = dealer_balances[0]
            dealer_balance.amount -= final_price
            dealer_balance.save()

        dealer_cars = dealer_profile.dealer_dealer_car.only('amount')
        if dealer_cars:
            dealer_car = dealer_cars[0]
            dealer_car.amount += desired_amount
            dealer_car.save()

        vendor.amount -= desired_amount
        vendor.save()
