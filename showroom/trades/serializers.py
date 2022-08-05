from rest_framework import serializers

from trades.models import Balance, Currency
from users.serializers import UserProfileSerializer


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id', 'name', 'created_at')


class BalanceSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()
    profile = UserProfileSerializer()

    class Meta:
        model = Balance
        fields = ('id', 'amount', 'currency', 'profile', 'created_at')
