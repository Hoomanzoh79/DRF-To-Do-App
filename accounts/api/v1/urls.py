from django.urls import path
from . import views

urlpatterns = [
    # registration
    path('registration/',views.RegistrationApiView.as_view(),name='registration'),

    # token login
    path('token/login/',views.TokenLoginApiView.as_view(),name='token-login'),
    # token logout
    path('token/logout/',views.TokenDiscardApiView.as_view(),name='token-logout'),
    # jwt token login

    # change password

    # profile page

    # reset password
]