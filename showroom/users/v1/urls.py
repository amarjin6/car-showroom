from django.urls import path

from rest_framework import routers
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView

from users.v1.views import UserProfileViewSet

router = routers.SimpleRouter()
router.register(r'', UserProfileViewSet)

urlpatterns = [
                  path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('verify_token/', TokenVerifyView.as_view(), name='token_verify'),
              ] + router.urls
