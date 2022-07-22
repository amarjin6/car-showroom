from django.db import models
from django.contrib.auth.models import User


class AbstractModel(models.Model):
    is_active = models.BooleanField(default=False)
    last_update = models.DateTimeField()
    instance_time = models.TimeField()

    class Meta:
        abstract = True


class ShowRoom(AbstractModel):
    name = models.CharField(max_length=30)
    location = models.IntegerField(default=0)
    customers = models.TextField(default='')
    history = models.TextField(default='')

    def __str__(self):
        return self.name


class Promotion(AbstractModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    discount = models.IntegerField(default=0)
    dealer = models.ManyToManyField(ShowRoom)

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


class Customer(AbstractModel):
    history = models.TextField(default='')
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile


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


class Offer(AbstractModel):
    max_price = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner


class Vendor(AbstractModel):
    foundation_year = models.DateTimeField()
    customers_amount = models.IntegerField(default=0)
    location = models.IntegerField(default=0)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile


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
