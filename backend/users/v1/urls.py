from rest_framework import routers

from users.v1.views import UserProfileViewSet
from orders.views import CustomerOrderViewSet, DealerOrderViewSet
from trades.views import BalanceViewSet
from promotions.views import PromotionViewSet
from dealer.views import DealerViewSet
from cars.views import CarViewSet

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'customer/orders', CustomerOrderViewSet)
router.register(r'dealer/orders', DealerOrderViewSet)
router.register(r'balances', BalanceViewSet)
router.register(r'promotions', PromotionViewSet)
router.register(r'dealers', DealerViewSet)
router.register(r'cars', CarViewSet)

urlpatterns = router.urls
