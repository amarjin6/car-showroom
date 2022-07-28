from django.db import models
from django.contrib.auth.models import User

from core.abstract_models import ModelProperties
from cars.models import Car


class UserProfile(ModelProperties):
    PROFILE_CHOICES = [('n', 'none'), ('c', 'customer'), ('v', 'vendor')]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, )
    profile = models.CharField(max_length=1, choices=PROFILE_CHOICES, default='n', blank=False)

    def __str__(self):
        name = self.user.username
        if self.profile == 'c':
            name = f'customer {name}'

        elif self.profile == 'v':
            name = f'vendor {name}'

        return name


class UserProfileCar(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='profile_userprofilecar')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_userprofilecar')
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.car_id.model} {self.amount}'
