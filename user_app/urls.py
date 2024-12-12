from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.my_signup_page, name='my_signup'),
    path("profile/", views.profile_page, name='profile'),
]