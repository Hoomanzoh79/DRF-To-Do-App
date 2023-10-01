from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # registration
    path("registration/", views.RegistrationApiView.as_view(), name="registration"),
    # token login
    path("token/login/", views.TokenLoginApiView.as_view(), name="token-login"),
    # token logout
    path("token/logout/", views.TokenDiscardApiView.as_view(), name="token-logout"),
    # jwt token login
    path("jwt/create/", views.CustomTokenObtainPairView.as_view(), name="jwt-create"),
    # jwt token refresh
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    # jwt token verify
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
    # change password
    path(
        "password/change/",
        views.ChangePasswordApiView.as_view(),
        name="password-change",
    ),
    # profile page
    path("profile/", views.ProfileApiView.as_view(), name="profile"),
    # reset password
]
