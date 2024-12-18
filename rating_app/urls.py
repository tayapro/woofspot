from django.urls import path
from . import views

urlpatterns = [
    path("create/<slug:slug>/", views.rate_create, name="rate_create"),
]