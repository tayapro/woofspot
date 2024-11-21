from django.urls import path
from . import views


urlpatterns = [
    path("", views.login_new_page, name='login_new'),
    path("logout_new/", views.logout_new_page, name='logout_new'),
    # TODO: add url for profile 
]