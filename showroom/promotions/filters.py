from django_filters import rest_framework as filters

from promotions.models import Promotion


class PromotionFilter(filters.FilterSet):
    is_active = filters.BooleanFilter(field_name='is_active')

    class Meta:
        model = Promotion
        fields = ['is_active']
