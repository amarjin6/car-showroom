from rest_framework import routers
from ..views import UserProfileViewSet
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView
from django.urls import path

router = routers.SimpleRouter()
router.register(r'list', UserProfileViewSet)

urlpatterns = [
                  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
              ] + router.urls
