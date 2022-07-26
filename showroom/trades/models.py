from django.db import models

from core.abstract_models import ModelProperties
from users.models import UserProfile


class Currency(ModelProperties):
    acronym = models.CharField(max_length=3, default='USD')
    name = models.CharField(max_length=30, default='US Dollar')

    def __str__(self):
        return self.acronym


class Balance(ModelProperties):
    amount = models.FloatField(default=.0)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.amount} {self.currency}'
