from django_filters import rest_framework as filters

from cars.models import Car


class CarFilter(filters.FilterSet):
    min_horsepower = filters.NumberFilter(field_name='specification__horsepower', lookup_expr='gte')
    max_horsepower = filters.NumberFilter(field_name='specification__horsepower', lookup_expr='lte')
    is_active = filters.BooleanFilter(field_name='is_active')
    created_at = filters.DateTimeFromToRangeFilter(field_name='created_at')

    class Meta:
        model = Car
        fields = ['min_horsepower', 'max_horsepower', 'is_active', 'created_at']
