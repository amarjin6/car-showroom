from django.db import models

from core.abstract_models import ModelProperties
from users.models import UserProfile
from dealer.models import Dealer


class Currency(ModelProperties):
    acronym = models.CharField(max_length=3, default='USD')
    name = models.CharField(max_length=30, default='US Dollar')

    def __str__(self):
        return self.acronym


class Balance(ModelProperties):
    amount = models.FloatField(default=.0)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.amount} {self.currency}'
