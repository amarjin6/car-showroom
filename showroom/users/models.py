from django.db import models
from django.contrib.auth.models import User


class AbstractModel(models.Model):
    is_active = models.BooleanField(default=False)
    lastUpdate = models.DateTimeField()
    instanceTime = models.TimeField()

    class Meta:
        abstract = True


class ShowRoom(models.Model, AbstractModel):
    name = models.CharField(max_length=30)
    location = models.IntegerField(default=0)
    customers = models.TextField(default='')
    history = models.TextField(default='')

    def __str__(self):
        return self.name


class Promotion(models.Model, AbstractModel):
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    discount = models.IntegerField(default=0)
    dealer = models.ForeignKey(ShowRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.discount


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


class Customer(models.Model, AbstractModel):
    history = models.TextField(default='')
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile


class Balance(models.Model, AbstractModel):
    amount = models.FloatField(default=.0)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dealer = models.ForeignKey(ShowRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner


class Currency(models.Model, AbstractModel):
    acronym = models.CharField(max_length=3)
    name = models.CharField(max_length=30)
    amount = models.ForeignKey(Balance, on_delete=models.CASCADE)

    def __str__(self):
        return self.amount


class Offer(models.Model, AbstractModel):
    maxPrice = models.IntegerField(default=0)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner


class Vendor(models.Model, AbstractModel):
    foundationYear = models.DateTimeField()
    customersAmount = models.IntegerField(default=0)
    address = models.CharField(max_length=60)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile


class Car(models.Model, AbstractModel):
    price = models.IntegerField(default=0)
    model = models.CharField(max_length=60)
    amount = models.IntegerField(default=0)
    order = models.ForeignKey(Offer, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    dealer = models.ForeignKey(ShowRoom, on_delete=models.CASCADE())

    def __str__(self):
        return self.order


class CarSpecifications(models.Model, AbstractModel):
    engine = models.CharField(max_length=60)
    horsepower = models.IntegerField(default=0)
    torque = models.IntegerField(default=0)
    transmission = models.TextField()
    overclocking = models.IntegerField(default=0)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.car
