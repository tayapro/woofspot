from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_started_page, name='get_started'),
    path("logout_new/", views.logout_new_page, name='logout_new'),
    # TODO: add url for profile 
]