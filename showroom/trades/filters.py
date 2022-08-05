from django_filters import rest_framework as filters

from trades.models import Balance


class BalanceFilter(filters.FilterSet):
    is_active = filters.BooleanFilter(field_name='is_active')
    created_at_from = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_at_to = filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Balance
        fields = ['is_active', 'created_at_from', 'created_at_to']
