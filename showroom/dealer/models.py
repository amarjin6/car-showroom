from django.db import models

from django_countries.fields import CountryField

from core.abstract_models import ModelProperties
from cars.models import Car


class Dealer(ModelProperties):
    name = models.CharField(max_length=30)
    location = CountryField(blank_label='select country')
    customers = models.TextField(default='')
    history = models.TextField(default='')
    car = models.ManyToManyField(Car, blank=True)

    def __str__(self):
        return self.name
