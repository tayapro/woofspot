from django.urls import path
from . import views

urlpatterns = [
    path("", views.carousel_event_list, name="home"),
    path("my/event/list/", views.my_event_list, name="my_event_list"),
    path("my/event/search/", views.my_event_search_results, name="my_event_search_results"),
    path("event/search/", views.event_search_results, name="event_search_results"),
    path("reservation/submit/<slug:slug>/", views.reservation_submit, name="reservation_submit"),
    path("reservation/cancel/<slug:slug>/", views.reservation_cancel, name="reservation_cancel"),
    path("like_toggle/<slug:slug>/", views.like_toggle, name="like_toggle"),
    path("event/create/", views.event_create, name="event_create"),
    path("event/view/<slug:slug>/", views.event_view, name="event_view"), 
    path("event/edit/<slug:slug>/", views.event_edit, name="event_edit"),
    path("event/delete/<slug:slug>/", views.event_delete, name="event_delete"),
    path("all/events/list/", views.all_events_list, name="all_events_list"),
    path("rating/submit/<slug:slug>/", views.rating_submit, name="rating_submit"),
]