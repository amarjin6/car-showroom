from django.contrib import admin

from orders.models import OrderVendorToDealer, OrderDealerToCustomer

admin.register(OrderDealerToCustomer)
admin.register(OrderVendorToDealer)
