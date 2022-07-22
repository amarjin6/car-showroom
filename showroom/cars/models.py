from django.db import models


class Car(AbstractModel):
    price = models.IntegerField(default=0)
    model = models.CharField(max_length=60)
    amount = models.IntegerField(default=0)
    order = models.ForeignKey(Offer, on_delete=models.CASCADE)
    vendor = models.ManyToManyField(Vendor)
    dealer = models.ManyToManyField(ShowRoom)

    def __str__(self):
        return self.order


class CarSpecifications(AbstractModel):
    engine = models.CharField(max_length=60)
    horsepower = models.IntegerField(default=0)
    torque = models.IntegerField(default=0)
    transmission = models.TextField()
    overclocking = models.IntegerField(default=0)
    car = models.ManyToManyField(Car)

    def __str__(self):
        return self.car
