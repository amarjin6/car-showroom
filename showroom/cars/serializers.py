from rest_framework import serializers

from cars.models import Car, CarSpecification


class CarSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecification
        fields = ('id', 'name', 'engine', 'horsepower', 'torque', 'transmission', 'overclocking', 'created_at')


class CarSerializer(serializers.ModelSerializer):
    specification = CarSpecificationSerializer()

    class Meta:
        model = Car
        fields = ('id', 'model', 'specification', 'created_at')
