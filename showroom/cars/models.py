from django.db import models
from core.abstract_models import ModelProperties


class CarSpecification(ModelProperties):
    engine = models.CharField(max_length=60)
    horsepower = models.IntegerField(default=0)
    torque = models.IntegerField(default=0)
    transmission = models.TextField()
    overclocking = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}'


class Car(ModelProperties):
    price = models.IntegerField(default=0)
    model = models.CharField(max_length=60)
    amount = models.IntegerField(default=0)
    specification = models.ManyToManyField(CarSpecification)

    def __str__(self):
        return self.model
