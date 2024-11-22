from django.urls import path
from . import views


urlpatterns = [
    path("get-started/", views.get_started_page, name='get_started'),
    path("logout-new/", views.logout_new_page, name='logout_new'),
    # TODO: add url for profile 
]