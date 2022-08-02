from django.db import models
from django.contrib.auth.models import User
from enum import Enum

from core.abstract_models import ModelProperties
from cars.models import Car


class Profile(Enum):
    NONE = 'none'
    CUSTOMER = 'customer'
    VENDOR = 'vendor'
    DEALER = 'dealer'

    @classmethod
    def choices(cls):
        return [(attr.value, attr.name) for attr in cls]

    def __str__(self):
        return self.value


class UserProfile(ModelProperties):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, )
    profile = models.CharField(max_length=8, choices=Profile.choices(), default=Profile.NONE.value, blank=False)

    def __str__(self):
        name = self.user.username
        if self.profile == Profile.CUSTOMER.value:
            name = f'customer {name}'

        elif self.profile == Profile.VENDOR.value:
            name = f'vendor {name}'

        elif self.profile == Profile.DEALER.value:
            name = f'dealer {name}'

        return name


class UserProfileCar(ModelProperties):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='profile_user_profile_car')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_user_profile_car')
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.profile.user.username} {self.car.model}'
