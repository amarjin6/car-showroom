from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from users.models import UserProfile
from users.serializers import UserProfileSerializer


class UserProfileViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)
