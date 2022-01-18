from . import views

# Импортируем из приложения django.contrib.auth нужный view-класс
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import path

app_name = "users"

urlpatterns = [
    path(
        "logout/",
        LogoutView.as_view(template_name="users/logged_out.html"),
        name="logout",
    ),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path(
        "login/",
        LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "password_reset/",
        PasswordResetView.as_view(template_name="users/password_reset_form.html"),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            # template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_confirm/done/",
        PasswordResetCompleteView.as_view(
            # template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
