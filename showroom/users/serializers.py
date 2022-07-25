from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'id', 'username', 'first_name', 'last_name', 'email', 'is_customer', 'is_vendor', 'is_active',
            'created_at',
            'last_update')
