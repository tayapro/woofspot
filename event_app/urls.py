from django.urls import path
from . import views

urlpatterns = [
    path('', views.FetchEvents.as_view(), name="home"),
    path('myevents/', views.events_page, name="events"),
    path('search/', views.search_results_page, name="search_results"),
    path('myevents/cancel/<slug:slug>/', views.cancel_event_page, name="cancel_event"),
    path('<slug:slug>/', views.event_detail_page, name="event_detail"),
]