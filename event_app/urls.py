from django.urls import path
from . import views

urlpatterns = [
    path('', views.FetchEvents.as_view(), name="home"),
    path('myevents/', views.events_page, name="events"),
    path('myevents/cancel/<slug:slug>/', views.cancel_event_page, name="cancel-event"),
    path('<slug:slug>/', views.event_detail, name="event-detail"),
]