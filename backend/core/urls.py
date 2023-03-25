from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from . import views

urlpatterns = [
    # authentication
    path("auth/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # oauth
    path("oauth/", views.OAuthCreate.as_view(), name="oauth"),
    path("oauth/profile/", views.OAuthProfile.as_view(), name="oauth_profile"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
