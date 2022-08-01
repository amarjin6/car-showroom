from rest_framework import routers

from users.v1.views import UserProfileViewSet
from orders.views import CustomerOrderViewSet

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'customer/orders', CustomerOrderViewSet)

urlpatterns = router.urls
