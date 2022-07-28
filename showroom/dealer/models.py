from django.db import models
from django_countries.fields import CountryField

from core.abstract_models import ModelProperties
from cars.models import Car
from users.models import UserProfile


class Dealer(ModelProperties):
    name = models.CharField(max_length=30)
    location = CountryField(blank_label='select country')
    profile = models.ManyToManyField(UserProfile, blank=True)
    history = models.TextField(default='')

    def __str__(self):
        return self.name


class DealerCar(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='dealer_dealer_car')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_dealer_car')
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.dealer.name} {self.car.model}'
