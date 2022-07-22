from django.db import models


class Customer(AbstractModel):
    history = models.TextField(default='')
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile
