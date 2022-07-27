from django.db import models
from django.contrib.auth.models import User

from core.abstract_models import ModelProperties


class UserProfile(ModelProperties):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, )
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

    def __str__(self):
        name = self.user.username
        if self.is_customer:
            name = f'customer {name}'

        elif self.is_vendor:
            name = f'vendor {name}'

        return name
