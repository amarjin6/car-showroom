from django_filters import rest_framework as filters

from promotions.models import Promotion


class PromotionFilter(filters.FilterSet):
    min_discount = filters.NumberFilter(field_name='discount', lookup_expr='gte')
    max_discount = filters.NumberFilter(field_name='discount', lookup_expr='lte')
    is_active = filters.BooleanFilter(field_name='is_active')
    created_at = filters.DateTimeFromToRangeFilter(field_name='created_at')

    class Meta:
        model = Promotion
        fields = ['min_discount', 'max_discount', 'is_active', 'created_at']
