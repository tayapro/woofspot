from django.urls import path
from . import views

urlpatterns = [
    path('', views.FetchEvents.as_view(), name="home"),
    path('<slug:slug>/', views.event_detail, name="event-detail"),
]