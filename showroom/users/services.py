from django_filters import rest_framework as filters

from users.models import UserProfile
from core.enums import Profile


class USerProfileFilter(filters.FilterSet):
    profile = filters.ChoiceFilter(choices=Profile.choices())
    is_active = filters.BooleanFilter(field_name='is_active')

    class Meta:
        model = UserProfile
        fields = ['profile', 'is_active']
