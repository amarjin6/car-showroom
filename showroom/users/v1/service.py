# from django.db import models
# from rest_framework import serializers
#
# from users.models import UserProfile
# from trades.models import Balance
# from dealer.models import Dealer
# from cars.models import Car
#
#
# class Order(models.Model):
#     number = serializers.IntegerField()
#     created = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=16)
#
#     def update_status(self, status: str) -> None:
#         self.status = status
#         self.save(update_fields=('status',))
#
#     def create(self, creator: UserProfile, item: Car, receiver:):
#
#
# def create_order(data: dict) -> bool:
#     if check_data(data):
#         order = Order.objects.create(data)
#
#     return False
#
#
# def check_data(data: dict) -> bool:
#     return True
#
#
# def order_get_by_user(user: UserProfile) -> Iterable[Order]:
#     return Order.objects.filter(user=user)
