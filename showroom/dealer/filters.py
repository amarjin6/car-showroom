from django_filters import rest_framework as filters

from dealer.models import Dealer


class DealerFilter(filters.FilterSet):
    is_active = filters.BooleanFilter(field_name='is_active')

    class Meta:
        model = Dealer
        fields = ['is_active']
