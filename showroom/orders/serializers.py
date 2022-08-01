from rest_framework import serializers
from typing import Dict

from orders.models import CustomerOrder
from orders.services import process_customer_order, check_customer_order
from users.serializers import UserProfileSerializer
from cars.serializers import CarSerializer
from users.models import UserProfile
from cars.models import Car, CarSpecification


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
