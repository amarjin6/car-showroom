from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from users.models import UserProfile
from orders.models import CustomerOrder, DealerOrder
from orders.serializers import CustomerOrderSerializer, ActionCustomerOrderSerializer, DealerOrderSerializer, \
    ActionDealerOrderSerializer
from core.permissions.permissions import IsCustomer, IsDealer, IsCustomerOrAdmin, IsDealerOrAdmin
from core.mixins.permissions import PermissionMixin
from core.mixins.serializers import DynamicSerializerMixin
from orders.filters import CustomerOrderFilter, DealerOrderFilter


class CustomerOrderViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, PermissionMixin,
                           DynamicSerializerMixin, viewsets.GenericViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer

    permission_classes = [IsCustomerOrAdmin]
    permissions_mapping = {
        'create': IsCustomer,
    }

    serializer_action_classes = {
        'create': ActionCustomerOrderSerializer,
        'list': CustomerOrderSerializer
    }

    filter_backends = (DjangoFilterBackend,)
    filterset_class = CustomerOrderFilter

    def create(self, request, *args, **kwargs):
        data = {**request.data, 'customer': UserProfile.objects.get(user_id=self.request.user.id).id}
        serializer = self.get_serializer_class()
        serializer = serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DealerOrderViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, PermissionMixin,
                         DynamicSerializerMixin, viewsets.GenericViewSet):
    queryset = DealerOrder.objects.all()
    serializer_class = DealerOrderSerializer

    permission_classes = [IsDealerOrAdmin]
    permissions_mapping = {
        'create': IsDealer
    }

    serializer_action_classes = {
        'create': ActionDealerOrderSerializer,
        'list': DealerOrderSerializer
    }

    filter_backends = (DjangoFilterBackend,)
    filterset_class = DealerOrderFilter

    def create(self, request, *args, **kwargs):
        data = {**request.data,
                'dealer': UserProfile.objects.get(user_id=self.request.user.id).profile_dealer.id}
        serializer = self.get_serializer_class()
        serializer = serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
