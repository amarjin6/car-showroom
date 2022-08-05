from django_filters import rest_framework as filters

from cars.models import Car


class CarFilter(filters.FilterSet):
    is_active = filters.BooleanFilter(field_name='is_active')

    class Meta:
        model = Car
        fields = ['is_active']
