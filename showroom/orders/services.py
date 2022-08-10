from typing import Dict, Tuple
from datetime import datetime
from celery import shared_task

from dealer.models import Dealer, DealerCar
from users.models import UserProfile, UserProfileCar
from orders.models import CustomerOrder, DealerOrder
from trades.models import Balance
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


def find_best_deal(clients, desired_price, car, profile) -> Tuple:
    first_client = None
    for suitable_client in clients:
        if suitable_client.price <= desired_price:
            first_client = suitable_client
            break

    if first_client:
        min_price = first_client.price

        for potential_client in clients:
            if profile == Profile.DEALER.value:
                promotion = potential_client.dealer.dealer_promotion.filter(car=car).order_by(
                    'discount').first()

            else:
                promotion = potential_client.profile.vendor_promotion.filter(car=car).order_by(
                    'discount').first()

            if promotion:
                start_date = promotion.start_date
                end_date = promotion.end_date
                discount = promotion.discount
                if start_date <= datetime.now() <= end_date:
                    client_price = potential_client.price * (1 - (discount / 100))
                    if client_price < min_price:
                        first_client = potential_client
                        min_price = client_price

        return first_client, min_price

    return None, 0


@shared_task
def process_customer_order() -> bool:
    orders = CustomerOrder.objects.all()
    for order in orders:
        if order.is_active:
            customer_profile = order.customer
            car_profile = order.car
            desired_amount = order.amount
            desired_price = order.price / desired_amount
            dealers = DealerCar.objects.select_related('dealer').filter(amount__gte=desired_amount,
                                                                        car=car_profile).order_by('price')

            dealer, min_price = find_best_deal(dealers, desired_price, car_profile, Profile.DEALER.value)
            if dealer:
                final_price = min_price * desired_amount

                dealer_balance = dealer.dealer.profile.profile_balance.only('amount').first()
                if dealer_balance:
                    dealer_balance.amount += final_price
                    dealer_balance.save()

                else:
                    new_balance = Balance(amount=final_price,
                                          currency=customer_profile.profile_balance.only('currency').first().currency,
                                          profile=dealer.dealer.profile)
                    new_balance.save()

                dealer.amount -= desired_amount
                dealer.save()

                customer_balance = customer_profile.profile_balance.only('amount').first()
                customer_balance.amount -= final_price
                customer_balance.save()

                order.is_active = False
                order.save()

                return True

            return False

        return True


@shared_task
def process_dealer_order() -> bool:
    orders = DealerOrder.objects.all()
    for order in orders:
        if order.is_active:
            dealer_profile = order.dealer
            car_profile = order.car
            desired_amount = order.amount
            desired_price = order.price / desired_amount
            vendors = UserProfileCar.objects.select_related('profile').filter(amount__gte=desired_amount,
                                                                              car__id=car_profile.id).order_by('price')

            vendor, min_price = find_best_deal(vendors, desired_price, car_profile, Profile.VENDOR.value)
            if vendor:
                final_price = min_price * desired_amount
                dealer_balance = dealer_profile.profile.profile_balance.only('amount').first()
                dealer_balance.amount -= final_price
                dealer_balance.save()

                dealer_car = dealer_profile.dealer_dealer_car.only('amount').filter(car_id=car_profile.id).first()
                if dealer_car:
                    dealer_car.amount += desired_amount
                    dealer_car.save()

                else:
                    new_car = DealerCar(dealer=dealer_profile, car=car_profile, amount=desired_amount,
                                        price=min_price * 1.1)
                    new_car.save()

                vendor.amount -= desired_amount
                vendor.save()

                order.is_active = False
                order.save()

                return True

            return False

    return True
