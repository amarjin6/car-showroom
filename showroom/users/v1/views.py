from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import AllowAny

from users.models import UserProfile
from users.serializers import UserProfileSerializer, RegisterUserProfileSerializer
from core.mixins.permissions import PermissionMixin
from core.permissions.permissions import IsOwnerOrAdmin


class UserProfileViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                         mixins.ListModelMixin, PermissionMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    # serializer_class = UserProfileSerializer
    permissions_mapping = {
        ('update', 'partial_update'): IsOwnerOrAdmin,
        ('create',): AllowAny,
    }
    permission_classes = (AllowAny, IsOwnerOrAdmin)
    serializer_action_classes = {
        'list': UserProfileSerializer,
        'create': RegisterUserProfileSerializer,
    }

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserProfileSerializer
        elif self.request.method == 'POST':
            return RegisterUserProfileSerializer


# class RegisterUserProfileViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
#     queryset = UserProfile.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = RegisterUserProfileSerializer
