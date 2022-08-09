from typing import Dict
from datetime import datetime

from dealer.models import Dealer, DealerCar
from users.models import UserProfile, UserProfileCar
from orders.models import CustomerOrder, DealerOrder
from promotions.models import Promotion
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
        if order.is_active:
            customer_profile = order.customer
            car_profile = order.car
            desired_amount = order.amount
            desired_price = order.price / desired_amount
            dealers = DealerCar.objects.select_related('dealer').filter(price__lte=desired_price,
                                                                        amount__gte=desired_amount,
                                                                        car__id=car_profile.id).order_by('price')
            if dealers:
                dealer = dealers[0]
                min_price = dealer.price
                for potential_dealer in dealers:
                    promotion = potential_dealer.dealer_promotion.filter(car=car_profile).order_by('discount')
                    if promotion:
                        start_date = promotion.start_date
                        end_date = promotion.end_date
                        discount = promotion.discount
                        if end_date <= datetime.now() >= start_date:
                            dealer_price = potential_dealer.price * (1 - (discount / 100))
                            if dealer_price < min_price:
                                dealer = potential_dealer
                                min_price = dealer_price

                final_price = min_price * desired_amount

                dealer_balance = dealer.dealer.profile.profile_balance.only('amount').first()
                if dealer_balance:
                    dealer_balance.amount += final_price
                    dealer.amount -= desired_amount
                    dealer.save()
                    dealer_balance.save()

                    customer_balance = customer_profile.profile_balance.only('amount').first()
                    customer_balance.amount -= final_price
                    customer_balance.save()

                    order.is_active = False
                    order.save()

                    return True

                return False

            return False

    return True


def process_dealer_order() -> bool:
    orders = DealerOrder.objects.all()
    for order in orders:
        if order.is_active:
            dealer_profile = order.dealer
            car_profile = order.car
            desired_amount = order.amount
            desired_price = order.price / desired_amount
            vendor = UserProfileCar.objects.select_related('profile').filter(price__lte=desired_price,
                                                                             amount__gte=desired_amount,
                                                                             car__id=car_profile.id).order_by(
                'price').first()

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
                    new_car = DealerCar(dealer=dealer_profile, car=car_profile, amount=desired_amount,
                                        price=vendor.price * 1.1)
                    new_car.save()

                vendor.amount -= desired_amount
                vendor.save()

                order.is_active = False
                order.save()

                return True

            return False

    return True
