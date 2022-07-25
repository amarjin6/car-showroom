from rest_framework import viewsets
from users.models import UserProfile
from users.serializers import UserProfileSerializer
from users.permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)
