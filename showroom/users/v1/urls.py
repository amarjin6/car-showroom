from rest_framework import routers

from users.v1.views import UserProfileViewSet

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet)

urlpatterns = router.urls
