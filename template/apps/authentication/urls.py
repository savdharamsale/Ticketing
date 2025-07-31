from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import AuthView, UserLoginView, UserRegisterView


urlpatterns = [
    path("auth/login/", UserLoginView.as_view(), name="auth-login-basic"),
    path("auth/register/", UserRegisterView.as_view(), name="auth-register-basic"),
    path(
        "auth/logout/",
        LogoutView.as_view(next_page="auth-login-basic"),
        name="auth-logout",
    ),
    path(
        "auth/forgot_password/",
        AuthView.as_view(template_name="auth_forgot_password_basic.html"),
        name="auth-forgot-password-basic",
    ),
]
