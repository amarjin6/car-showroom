from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer
from .permissions import IsAdminOrReadOnly


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAdminOrReadOnly,)
