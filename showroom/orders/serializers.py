from rest_framework import serializers

from orders.models import CustomerOrder
from orders.services import process_customer_order
from users.serializers import UserProfileSerializer
from cars.serializers import CarSerializer


class CustomerOrderSerializer(serializers.ModelSerializer):
    customer = UserProfileSerializer()
    car = CarSerializer()

    class Meta:
        model = CustomerOrder
        fields = ('id', 'price', 'amount', 'customer', 'car', 'created_at')


class ActionCustomerOrderSerializer(serializers.ModelSerializer):
    customer = UserProfileSerializer()
    car = CarSerializer()

    class Meta:
        model = CustomerOrder
        fields = ('id', 'price', 'amount', 'customer', 'car', 'created_at')

    def validate(self, attrs):
        ...

    def create(self, validated_data):
        process_customer_order(validated_data)
