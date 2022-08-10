from django.db import models

from core.abstract_models import ModelProperties
from dealer.models import Dealer
from users.models import UserProfile
from cars.models import Car


class Promotion(ModelProperties):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=30)
    description = models.TextField(default='')
    discount = models.IntegerField(default=0)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='dealer_promotion')
    vendor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='vendor_promotion')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_promotion')

    def __str__(self):
        return f'{self.name} {self.dealer.name} {self.car.model} {self.discount}%'
