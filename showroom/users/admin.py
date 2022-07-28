from django.contrib import admin

from users.models import UserProfile, UserProfileCar

admin.site.register(UserProfile)
admin.site.register(UserProfileCar)
