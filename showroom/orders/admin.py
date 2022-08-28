from django.contrib import admin

from orders.models import DealerOrder, CustomerOrder

admin.site.register(CustomerOrder)
admin.site.register(DealerOrder)

