from django.db import models
from django.contrib.auth.models import User

from core.abstract_models import ModelProperties
from cars.models import Car

from trades.models import Balance


class UserProfile(ModelProperties):
    PROFILE_CHOICES = [('n', 'none'), ('c', 'customer'), ('v', 'vendor')]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, )
    profile = models.CharField(max_length=1, choices=PROFILE_CHOICES, default='n', blank=False)
    car = models.ManyToManyField(Car, blank=True)
    cars_amount = models.IntegerField(default=0)
    balance = models.OneToOneField(Balance, on_delete=models.CASCADE, null=True)

    def __str__(self):
        name = self.user.username
        if self.profile == 'c':
            name = f'customer {name}'

        elif self.profile == 'v':
            name = f'vendor {name}'

        return name
