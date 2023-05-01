from django.contrib import admin

from trades.models import Balance, Currency

admin.site.register(Balance)
admin.site.register(Currency)
