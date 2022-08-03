from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response

from users.models import UserProfile
from orders.models import CustomerOrder, DealerOrder
from orders.serializers import CustomerOrderSerializer, ActionCustomerOrderSerializer, DealerOrderSerializer, \
    ActionDealerOrderSerializer
from core.permissions.permissions import IsCustomer, IsDealer, IsCustomerOrAdmin, IsDealerOrAdmin
from core.mixins.permissions import PermissionMixin
from orders.services import process_dealer_order


class CustomerOrderViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, PermissionMixin,
                           viewsets.GenericViewSet):
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

    def create(self, request, *args, **kwargs):
        data = {**request.data, 'customer': UserProfile.objects.get(user_id=self.request.user.id).id}
        serializer = self.get_serializer_class()
        serializer = serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def get_serializer_class(self):
        return self.serializer_action_classes.get(self.action,
                                                  CustomerOrderSerializer)


class DealerOrderViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                         viewsets.GenericViewSet):
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

    def create(self, request, *args, **kwargs):
        data = {**request.data, 'dealer': UserProfile.objects.get(user_id=self.request.user).id}
        serializer = self.get_serializer_class()
        serializer = serializer(data=data)
        process_dealer_order(data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def get_serializer_class(self):
        return self.serializer_action_classes.get(self.action,
                                                  DealerOrderSerializer)
