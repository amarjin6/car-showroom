from rest_framework import viewsets
from rest_framework import mixins

from users.models import UserProfile
from users.serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from core.mixins.permissions import PermissionMixin
from core.permissions.permissions import IsOwnerOrAdmin


class UserProfileViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                         mixins.ListModelMixin, PermissionMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permissions_mapping = {
        ('update', 'partial_update'): IsOwnerOrAdmin,
    }
    permission_classes = (IsAuthenticated,)
