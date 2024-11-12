from django.urls import path
from . import views

urlpatterns = [
    path('', views.FetchEvents.as_view(), name='home'),
    path('<slug:slug>/', views.get_event, name="event-detail"),
]