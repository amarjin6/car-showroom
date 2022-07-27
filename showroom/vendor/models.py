from django.db import models
from django_countries.fields import CountryField

from core.abstract_models import ModelProperties
from users.models import UserProfile


class Vendor(ModelProperties):
    foundation_year = models.DateTimeField()
    customers_amount = models.IntegerField(default=0)
    location = CountryField(blank_label='(select country)')
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile
