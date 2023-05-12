from django_filters import rest_framework as filters

from trades.models import Balance


class BalanceFilter(filters.FilterSet):
    min_amount = filters.NumberFilter(field_name='amount', lookup_expr='gte')
    max_amount = filters.NumberFilter(field_name='amount', lookup_expr='lte')
    is_active = filters.BooleanFilter(field_name='is_active')
    created_at = filters.DateTimeFromToRangeFilter(field_name='created_at')

    class Meta:
        model = Balance
        fields = ['min_amount', 'max_amount', 'is_active', 'created_at']
