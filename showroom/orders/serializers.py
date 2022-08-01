from rest_framework import serializers
from typing import Dict

from orders.models import CustomerOrder, DealerOrder
from orders.services import process_customer_order, check_customer_order, check_dealer_order
from users.serializers import UserProfileSerializer
from cars.serializers import CarSerializer
from dealer.serializers import DealerSerializer


class CustomerOrderSerializer(serializers.ModelSerializer):
    customer = UserProfileSerializer()
    car = CarSerializer()

    class Meta:
        model = CustomerOrder
        fields = ('id', 'price', 'amount', 'customer', 'car', 'created_at')


class ActionCustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = ('price', 'amount', 'customer', 'car', 'created_at')

    def validate(self, attrs: Dict) -> Dict:
        if check_customer_order(attrs):
            return attrs

        raise serializers.ValidationError({400: "Bad Request!"})


class DealerOrderSerializer(serializers.ModelSerializer):
    dealer = DealerSerializer()
    car = CarSerializer()

    class Meta:
        model = DealerOrder
        fields = ('id', 'price', 'amount', 'dealer', 'car', 'created_at')


class ActionDealerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerOrder
        fields = ('price', 'amount', 'dealer', 'car', 'created_at')

    def validate(self, attrs: Dict) -> Dict:
        if check_dealer_order(attrs):
            return attrs

        raise serializers.ValidationError({400: "Bad Request!"})
