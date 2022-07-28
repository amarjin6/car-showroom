from django.db import models
from django_countries.fields import CountryField

from core.abstract_models import ModelProperties
from cars.models import Car
from trades.models import Balance
from users.models import UserProfile


class Dealer(ModelProperties):
    name = models.CharField(max_length=30)
    location = CountryField(blank_label='select country')
    profile = models.ManyToManyField(UserProfile, blank=True)
    history = models.TextField(default='')
    car = models.ManyToManyField(Car, blank=True)
    balance = models.OneToOneField(Balance, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
