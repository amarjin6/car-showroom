from django.db import models


class Promotion(AbstractModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    discount = models.IntegerField(default=0)
    dealer = models.ManyToManyField(ShowRoom)

    def __str__(self):
        return self.discount
