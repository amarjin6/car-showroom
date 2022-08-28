from django.db import models

from core.abstract_models import ModelProperties
from users.models import UserProfile
from core.enums import Acronym


class Currency(ModelProperties):
    name = models.CharField(max_length=3, choices=Acronym.choices(), default=Acronym.USD)

    def __str__(self):
        return self.name


class Balance(ModelProperties):
    amount = models.FloatField(default=.0)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_balance')
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='profile_balance')

    def __str__(self):
        return f'{self.amount} {self.currency} {self.profile.user}'
