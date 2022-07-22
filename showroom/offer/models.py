from django.db import models


class Offer(AbstractModel):
    max_price = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner
