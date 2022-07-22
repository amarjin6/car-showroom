from django.db import models


class Balance(AbstractModel):
    amount = models.FloatField(default=.0)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dealer = models.ForeignKey(ShowRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner


class Currency(AbstractModel):
    acronym = models.CharField(max_length=3)
    name = models.CharField(max_length=30)
    amount = models.ForeignKey(Balance, on_delete=models.CASCADE)

    def __str__(self):
        return self.amount
