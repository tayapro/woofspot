from django.urls import path
from allauth.account.views import PasswordResetView
from user_app.forms import CustomResetPasswordForm
from . import views


urlpatterns = [
    path("accounts/password/reset/",
        PasswordResetView.as_view(form_class=CustomResetPasswordForm),
        name="account_reset_password",
    ),
    path("profile/", views.profile, name='profile'),
]