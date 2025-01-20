from django.urls import path
from . import views

urlpatterns = [
    # Landing page that displays a carousel of events and includes the
    # Contact Us form
    path("", views.carousel_events_contact_us, name="home"),

    # List of events that the current user is associated with
    # (a host or attendee)
    path("my/event/list/", views.my_event_list, name="my_event_list"),

    # Search results for events based on query and scope
    # (all or user's scope events)
    path("event/search/", views.event_search_results,
         name="event_search_results"),

    # Submit a reservation for an event by its slug
    path("reservation/submit/<slug:slug>/", views.reservation_submit,
         name="reservation_submit"),

    # Cancel a reservation for an event by its slug
    path("reservation/cancel/<slug:slug>/", views.reservation_cancel,
         name="reservation_cancel"),

    # Toggle the "like" status for an event by its slug
    path("like_toggle/<slug:slug>/", views.like_toggle, name="like_toggle"),

    # Create a new event
    path("event/create/", views.event_create, name="event_create"),

    # View details for a specific event by its slug
    path("event/view/<slug:slug>/", views.event_view, name="event_view"),

    # Edit an existing event by its slug
    path("event/edit/<slug:slug>/", views.event_edit, name="event_edit"),

    # Delete an event by its slug
    path("event/delete/<slug:slug>/", views.event_delete, name="event_delete"),

    # Display a list of all events (future and past) for public browsing
    path("all/events/list/", views.all_events_list, name="all_events_list"),

    # Submit a rating for a specific event by its slug
    path("rating/submit/<slug:slug>/", views.rating_submit,
         name="rating_submit"),
]
