from rest_framework import routers

from users.v1.views import UserProfileViewSet
from orders.views import CustomerOrderViewSet, DealerOrderViewSet

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'customer/orders', CustomerOrderViewSet)
router.register(r'dealer/orders', DealerOrderViewSet)

urlpatterns = router.urls
