from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.models import UserProfile
from users.serializers import UserProfileSerializer
from core.mixins.permissions import ActivityViewSet


class UserProfileViewSet(viewsets.ModelViewSet, ActivityViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permissions_mapping = {
        ('update', 'partial_update'): IsAuthenticated,
    }

    permission_classes = (ActivityViewSet.get_permissions(permissions_mapping),)
