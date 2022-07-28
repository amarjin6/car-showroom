from django.db import models
from core.abstract_models import ModelProperties


class CarSpecification(ModelProperties):
    name = models.CharField(max_length=30)
    engine = models.CharField(max_length=60)
    horsepower = models.IntegerField(default=0)
    torque = models.IntegerField(default=0)
    transmission = models.TextField()
    overclocking = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Car(ModelProperties):
    price = models.IntegerField(default=0)
    model = models.CharField(max_length=60)
    specification = models.ForeignKey(CarSpecification, on_delete=models.CASCADE, related_name='car_car_specification')

    def __str__(self):
        return self.model
