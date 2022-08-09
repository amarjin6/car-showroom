from typing import Dict

from dealer.models import Dealer, DealerCar
from users.models import UserProfile, UserProfileCar
from orders.models import CustomerOrder, DealerOrder
from cars.models import Car
from core.enums import Profile


def check_order(client_name: str, attrs: Dict) -> bool:
    if client_name == Profile.CUSTOMER.value:
        user_profile = UserProfile.objects.get(id=attrs.get(client_name).id)
        balance = user_profile.profile_balance.only('amount').first()

    else:
        dealer_profile = Dealer.objects.get(id=attrs.get(client_name).id)
        balance = dealer_profile.profile.profile_balance.only('amount').first()

    if balance:
        client_balance = balance.amount
        price = attrs['price']

        return client_balance >= price

    return False


def process_customer_order() -> bool:
    orders = CustomerOrder.objects.all()
    for order in orders:
        customer_profile = UserProfile.objects.get(id=order.customer.id)
        car_profile = Car.objects.get(id=order.car)
        desired_amount = order['amount']
        desired_price = order['price'] / desired_amount
        dealer = DealerCar.objects.select_related('dealer').filter(price__lte=desired_price,
                                                                   amount__gte=desired_amount,
                                                                   car__id=car_profile.id).order_by('price').first()

        if dealer:
            final_price = dealer.price * desired_amount

            dealer_balance = dealer.dealer.profile.profile_balance.only('amount').first()
            if dealer_balance:
                dealer_balance.amount += final_price
                dealer.amount -= desired_amount
                dealer_balance.save()
                dealer.save()

                customer_balance = customer_profile.profile_balance.only('amount').first()
                customer_balance.amount -= final_price
                customer_balance.save()

            order.is_active = False
            order.save()

            return True

        return False

    return True


def process_dealer_order(order: Dict) -> bool:
    dealer_profile = Dealer.objects.get(id=order.get('dealer'))
    car_profile = Car.objects.get(id=order.get('car'))
    desired_amount = order['amount']
    desired_price = order['price'] / desired_amount
    vendor = UserProfileCar.objects.select_related('profile').filter(price__lte=desired_price,
                                                                     amount__gte=desired_amount,
                                                                     car__id=car_profile.id).order_by('price').first()

    if vendor:
        final_price = vendor.price * desired_amount

        dealer_balance = dealer_profile.profile.profile_balance.only('amount').first()
        dealer_balance.amount -= final_price
        dealer_balance.save()

        dealer_car = dealer_profile.dealer_dealer_car.only('amount').filter(car_id=car_profile.id).first()
        if dealer_car:
            dealer_car.amount += desired_amount
            dealer_car.save()

        else:
            new_car = DealerCar(dealer=dealer_profile, car=car_profile, amount=desired_amount, price=vendor.price * 1.1)
            new_car.save()

        vendor.amount -= desired_amount
        vendor.save()

        return True

    return False
