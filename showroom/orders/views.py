from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import UserProfile
from orders.models import CustomerOrder, DealerOrder
from orders.serializers import CustomerOrderSerializer, ActionCustomerOrderSerializer, DealerOrderSerializer, \
    ActionDealerOrderSerializer


class CustomerOrderViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    queryset = CustomerOrder.objects.all()
    serializer_class = CustomerOrderSerializer
    permission_classes = (IsAuthenticated,)
    serializer_action_classes = {
        'create': ActionCustomerOrderSerializer,
        'list': CustomerOrderSerializer
    }

    def create(self, request, *args, **kwargs):
        data = {**request.data, 'customer': UserProfile.objects.get(user_id=self.request.user).id}
        serializer = self.get_serializer_class()
        serializer = serializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        return self.serializer_action_classes.get(self.action,
                                                  CustomerOrderSerializer)


class DealerOrderViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = DealerOrder.objects.all()
    serializer_class = DealerOrderSerializer
    permission_classes = (IsAuthenticated,)
    serializer_action_classes = {
        'create': ActionDealerOrderSerializer,
        'list': DealerOrderSerializer
    }

    def create(self, request, *args, **kwargs):
        data = {**request.data, 'dealer': UserProfile.objects.get(user_id=self.request.user).id}
        serializer = self.get_serializer_class()
        serializer = serializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        return self.serializer_action_classes.get(self.action,
                                                  DealerOrderSerializer)
