from django.urls import path
from . import views


urlpatterns = [
    path("signin/", views.my_signin_page, name='my_signin'),
    path("signup/", views.my_signup_page, name='my_signup'),
    path("signout/", views.my_signout_page, name='my_signout'),
    path("profile/", views.profile_page, name='profile'),
]