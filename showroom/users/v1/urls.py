from django.urls import path

from rest_framework import routers
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView

from users.v1.views import UserProfileViewSet

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet)
# router.register(r'register', UserProfileViewSet)

urlpatterns = router.urls + [
                  # path('register/', RegisterUserProfileViewSet.as_view({'post': 'create'})),
                  path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('users/login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
                  path('users/login/verify', TokenVerifyView.as_view(), name='token_verify'),
              ]
