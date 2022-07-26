from django.db import models
from core.abstract_models import ModelProperties
from users.models import UserProfile


class Balance(ModelProperties):
    amount = models.FloatField(default=.0)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.amount


class Currency(ModelProperties):
    acronym = models.CharField(max_length=3)
    name = models.CharField(max_length=30)
    amount = models.ForeignKey(Balance, on_delete=models.CASCADE)

    def __str__(self):
        return self.acronym
