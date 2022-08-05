from django_filters import rest_framework as filters

from users.models import UserProfile
from core.enums import Profile


class UserProfileFilter(filters.FilterSet):
    profile = filters.ChoiceFilter(choices=Profile.choices())
    is_active = filters.BooleanFilter(field_name='is_active')
    created_at_from = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_at_to = filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = UserProfile
        fields = ['profile', 'is_active', 'created_at_from', 'created_at_to']
