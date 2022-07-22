from django.db import models
from django.contrib.auth.models import User


class UserProfile(User, AbstractModel):
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

    def __str__(self):
        name = self.username
        if self.is_customer:
            name = f'customer {name}'

        elif self.is_vendor:
            name = f'vendor {name}'

        return name
