from django.db import models

from core.abstract_models import ModelProperties
from users.models import UserProfile
from dealer.models import Dealer


class OrderDealerToCustomer(ModelProperties):
    price = models.FloatField(default=.0)
    amount = models.IntegerField(default=0)
    sender = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='sender_order_dealer_to_customer')
    receiver = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='receiver_order_dealer_to_customer')

    def __str__(self):
        return f'dealer {self.sender.name}, customer {self.receiver.user.username}'


class OrderVendorToDealer(ModelProperties):
    price = models.FloatField(default=.0)
    amount = models.IntegerField(default=0)
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='sender_order_vendor_to_dealer')
    receiver = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='receiver_order_vendor_to_dealer')

    def __str__(self):
        return f'vendor {self.sender.user.username}, dealer {self.receiver.name}'