from django_filters import rest_framework as filters

from dealer.models import Dealer


class DealerFilter(filters.FilterSet):
    location = filters.CharFilter(field_name='location')
    is_active = filters.BooleanFilter(field_name='is_active')
    created_at = filters.DateTimeFromToRangeFilter(field_name='created_at')

    class Meta:
        model = Dealer
        fields = ['location', 'is_active', 'created_at']
