from django.db import models

from core.abstract_models import ModelProperties
from dealer.models import Dealer


class Promotion(ModelProperties):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=30)
    description = models.TextField(default='')
    discount = models.IntegerField(default=0)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='dealer_promotion')

    def __str__(self):
        return f'{self.name} {self.dealer.name} {self.discount}%'
