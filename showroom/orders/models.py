from django.db import models

from core.abstract_models import ModelProperties
from users.models import UserProfile
from dealer.models import Dealer
from cars.models import Car


class CustomerOrder(ModelProperties):
    price = models.FloatField(default=.0)
    amount = models.IntegerField(default=1)
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='customer_customer_order')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_customer_order')

    def __str__(self):
        return f'customer {self.customer.user.username} car {self.car.model}'


class DealerOrder(ModelProperties):
    price = models.FloatField(default=.0)
    amount = models.IntegerField(default=1)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='dealer_dealer_order')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_dealer_order')

    def __str__(self):
        return f'dealer {self.dealer.name} car {self.car.model}'
