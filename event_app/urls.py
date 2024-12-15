from django.urls import path
from . import views

urlpatterns = [
    path('', views.FetchEvents.as_view(), name="home"),
    path("my/event/list/", views.my_event_list, name="my_event_list"),
    path("search/", views.search_results, name="search_results"), # search in all events
    # TODO: search in my/event/list
    path("reservation/cancel/<slug:slug>/", views.reservation_cancel, name="reservation_cancel"),
    path('toggle-like/<slug:slug>/', views.toggle_like, name="toggle_like"),
    path("event/create/", views.event_create, name="event_create"),
    path("event/<slug:slug>/", views.event_view, name="event_view"),
    path("event/edit/<slug:slug>/", views.event_edit, name="event_edit"),
    path("event/delete/<slug:slug>/", views.event_delete, name="event_delete"),
]