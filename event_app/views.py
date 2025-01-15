from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from django.utils.timezone import now
from datetime import time, datetime
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from .models import WoofspotEvent
from .forms import EventOrganizerForm
from .models import Rating
from .forms import ReviewForm
from .utils import validate_image_url, is_in_the_past, send_email, remove_leading_space


def get_event_image(event):
    if event.image and validate_image_url(event.image.url):
            image_url = event.image.url
    else:
            image_url = "https://res.cloudinary.com/stipaxa/image/upload/v1736449375/Woofspot/image_coming_soon_3.webp"

    return image_url

# def get_all_events(request):
#     return WoofspotEvent.objects.all()

# def get_all_past_events(events):
#     timestamp = now().date()

#     past_events = []
#     for event in events:
#         if(event.)

#     return past_events

def all_events_list(request):
    timestamp = now().date()
    events = WoofspotEvent.objects.all()

    future_events = WoofspotEvent.objects.filter(date__gt=timestamp)
    past_events = WoofspotEvent.objects.filter(date__lte=timestamp)

    for events in (future_events, past_events):
        for event in events:
            event.image_url = get_event_image(event)
            event.is_user_attendee = (request.user in event.attendees.all())
            event.average_rating = Rating.get_average_rating(event)

    next = request.GET.get("next", reverse("home"))

    return render(request, "event_app/all_events_list.html", {
        "future_events": future_events,
        "past_events": past_events,
        "next": next,
    })

def event_list(request):
    timestamp = now().date()

    events = WoofspotEvent.objects.filter(date__gt=timestamp)

    for event in events:
        event.image_url = get_event_image(event)
        event.is_user_attendee = (request.user in event.attendees.all())
        event.average_rating = Rating.get_average_rating(event)

    return render(request, "event_app/index.html", {
        "events": events,
    })


def event_view(request, slug):
    event = get_object_or_404(WoofspotEvent, slug=slug)
    event.image_url = get_event_image(event)

    event.average_rating = Rating.get_average_rating(event)

    event.is_past = is_in_the_past(event.date)
    event.is_user_attendee = (request.user in event.attendees.all())

    next = request.GET.get("next", reverse("my_event_list"))

    return render(
        request,
        "event_app/event_view.html",
        {
            "event": event,
            "next": next,
        },
    )


def my_event_list(request):
    user = request.user
    if not user.is_authenticated:
        return redirect(reverse("account_login"))

    timestamp = now().date()
    
    hosted_by_me_future_events = WoofspotEvent.objects.filter(
                                organizer=request.user,
                                date__gt=timestamp)
    planning_to_attend_events = WoofspotEvent.objects.filter(
                                attendees=request.user,
                                date__gt=timestamp)
    past_attending_events = WoofspotEvent.objects.filter(
                                attendees=request.user,
                                date__lte=timestamp)
    past_organizing_events = WoofspotEvent.objects.filter(
                                organizer=request.user,
                                date__lte=timestamp)
    past_events = list(past_attending_events) + list(past_organizing_events)
    past_events.sort(reverse=True, key=lambda e : (e.date, e.start_time))

    # Set image URLs and other parameters for all events 
    for events in (hosted_by_me_future_events, planning_to_attend_events, past_events):
        for event in events:
            event.image_url = get_event_image(event)
            event.is_past = is_in_the_past(event.date)
            event.is_user_attendee = (request.user in event.attendees.all())
            event.average_rating = Rating.get_average_rating(event)

    return render(request, "event_app/my_event_list.html",
                 {"user": user,
                  "hosted_by_me_future_events": hosted_by_me_future_events,
                  "planning_to_attend_events": planning_to_attend_events,
                  "past_events": past_events,
                 })


@login_required
def reservation_submit(request, slug):
    user = request.user
    event = get_object_or_404(WoofspotEvent, slug=slug)

    if request.method == "POST" and "reserve_spot" in request.POST:
        if request.user in event.attendees.all():
            messages.error(request, "You have already reserved a spot for this event.")
        else:
            event.attendees.add(request.user)
            messages.success(request, "Slot is reserved!")
            action = "Reservation Confirmed"
            send_email(user, event, action)

    return redirect(reverse("event_view", args=[slug]))


@login_required
def reservation_cancel(request, slug):
    user = request.user
    event = get_object_or_404(WoofspotEvent, slug=slug)
    next = request.GET.get("next", reverse("my_event_list"))

    if request.method == "POST" and "cancel_reservation" in request.POST:  
        event.attendees.remove(user)
        action = "Reservation Cancelled"
        send_email(user, event, action)

        messages.success(request, "Slot is canceled!")

        return redirect(reverse("my_event_list"))
        
    return render(request, "event_app/reservation_cancel.html",
    {
        "event": event,
        "user": user,
        "next": next
    })


def event_search_results(request):
    query = request.GET.get("query")  
    search_results = []
    if query:
        search_results = WoofspotEvent.objects.filter(
            Q(title__icontains=query) |  
            Q(description__icontains=query)  
        )
    next = request.GET.get("next", "/")

    for event in search_results:
        event.image_url = get_event_image(event)
        event.is_past = is_in_the_past(event.date)
        event.is_user_attendee = (request.user in event.attendees.all())
        event.average_rating = Rating.get_average_rating(event)

    return render(request,
                  "event_app/event_search_results.html", 
                  {
                    "next": next,
                    "query": query, 
                    "search_results": search_results
                  })


def my_event_search_results(request):
    user = request.user
    if not user.is_authenticated:
        return redirect(reverse("account_login"))
    
    events = WoofspotEvent.objects.filter(
        Q(attendees=user) | Q(organizer=user)
    )
    
    query = request.GET.get("query")  
    search_results = events
    if query:
        search_results = search_results.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    for event in search_results:
        event.image_url = get_event_image(event)
        event.is_past = is_in_the_past(event.date)
        event.is_user_attendee = (request.user in event.attendees.all())
        event.average_rating = Rating.get_average_rating(event)
    
    next = request.GET.get("next", reverse("my_event_list"))
    
    return render(request, 
                  "event_app/event_search_results.html",
                  {
                    "next": next,
                    "query": query,
                    "search_results": search_results
                  })

@login_required
def like_toggle(request, slug):
    event = get_object_or_404(WoofspotEvent, slug=slug)

    next = request.GET.get("next", "home")

    event.like_toggle(request.user)
    return render(request, "like_container.html", {
        "next": next,
        "event": event
    })


@login_required
def event_create(request):
    next = request.GET.get("next", reverse("my_event_list"))
    user = request.user

    # Handle submit (POST)
    if request.method == "POST":
        form = EventOrganizerForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)

            event.organizer = user

            remove_leading_space(event)
            
            if not event.title.isascii() or not event.description.isascii() or not event.location.isascii():
                form.add_error(None, "Please use only latin/accented characters")
                return render(request, "event_app/event_create.html", {"form": form, "next": next,})

            slug_base = slugify(event.title)
            slug = slug_base
            counter = 1
            # In case if slug for existing event with new title is equal to created one
            # generate a new slug
            while WoofspotEvent.objects.filter(slug=slug).exists():
                slug = f"{slug_base}-{counter}"
                counter += 1
            
            event.slug = slug

            try:
                event.full_clean()
                event.save()
                action = "Event Created"
                send_email(user, event, action)
                messages.success(request, "Event created successfully!")
                return redirect(next)
            except ValidationError as e:
                form.add_error(None, e.messages)
                return render(request, "event_app/event_create.html", {"form": form, "next": next,})
        else:
            form.add_error(None, "please make changes.")
            return render(request, "event_app/event_create.html", {"form": form, "next": next,})
    
    # Handle page (GET)
    form = EventOrganizerForm()   
    return render(request, "event_app/event_create.html", {
        "form": form,
        "next": next,
    })


@login_required
def event_edit(request, slug):
    user = request.user
    event = get_object_or_404(WoofspotEvent, slug=slug)
    next = request.GET.get("next", reverse("my_event_list"))

    if event.organizer != request.user:
        return HttpResponseForbidden("Unauthorized access")

    original_date = event.date
    original_start_time = event.start_time
    original_end_time = event.end_time

    # Handle submit (POST)
    if request.method == "POST":
        form = EventOrganizerForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            updated_event = form.save(commit=False)
            remove_leading_space(updated_event)

            if form.changed_data:
                if not updated_event.title.isascii() or not updated_event.description.isascii() or not updated_event.location.isascii():
                    form.add_error(None, "Please use only latin/accented characters")
                    return render(request, "event_app/event_create.html", {"form": form, "next": next,})    

                try:
                    event.full_clean()
                    updated_event.save()
                    action = "Event Changed"
                    send_email(user, updated_event, action)
                    messages.success(request, "Event updated successfully!")
                    return redirect(next)
                except ValidationError as e:
                    form.add_error(None, e.messages)
                    return render(request, "event_app/event_create.html", {"form": form, "event": event, "next": next,})
            else:
                form.add_error(None, "No changes detected.")
                return render(request, "event_app/event_edit.html", {"form": form, "event": event,
                                "next": next })

        else:
            form.add_error(None, "please make changes.")
            return render(request, "event_app/event_edit.html", {"form": form, "event": event,
                            "next": next })

    # Handle page (GET)
    form = EventOrganizerForm(instance=event)
    return render(request, "event_app/event_edit.html", {
        "form": form,
        "event": event,
        "next": next
    })


@login_required
def event_delete(request, slug):
    event = get_object_or_404(WoofspotEvent, slug=slug)
    user = request.user
    next = request.GET.get("next", reverse("my_event_list"))

    if event.organizer != request.user:
        return HttpResponseForbidden("Unauthorized access")
    
    if request.method == "POST" and "event_delete" in request.POST:
        # Delete related ratings
        Rating.objects.filter(event=event).delete()
        action = "Event Cancelled"
        send_email(user, event, action)
        event.delete()
        return redirect("my_event_list")
    
    return render(request, "event_app/event_delete.html",
    {
        "event": event,
        "next": next
    })


@login_required
def rating_submit(request, slug):
    event = get_object_or_404(WoofspotEvent, slug=slug)

    if event.organizer == request.user:
        return HttpResponseForbidden("Unauthorized access")

    next = request.GET.get("next", reverse("my_event_list"))

    # Handle submit (POST)
    if request.method == "POST":
        form = ReviewForm(request.POST, event=event)

        if form.is_valid():
            Rating.objects.filter(user=request.user, event=event).delete()

            rating = form.save(commit=False)
            rating.user = request.user
            rating.event = event
            rating.save()

            action = "Rating Created"
            send_email(rating.user, rating.event, action)

            return redirect("event_view", slug=event.slug)
        else:
            form.add_error(None, "Form is invalid. Please correct the errors below.")
            return render(request, "event_app/rating_submit.html", {"form": form, "event": event,
                            "next": next,})

    # Handle page (GET)
    form = ReviewForm(event=event)
    return render(request, "event_app/rating_submit.html", {"form": form, "event": event, "next": next})