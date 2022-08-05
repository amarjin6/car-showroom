from rest_framework import viewsets
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser

from trades.models import Balance
from trades.serializers import BalanceSerializer
from trades.filters import BalanceFilter


class BalanceViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Balance.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BalanceFilter
