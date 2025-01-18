from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q
from datetime import date, timedelta
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from .models import WoofspotEvent, Rating
from .forms import EventOrganizerForm, ContactUsForm, ReviewForm
from .utils import validate_image_url, is_in_the_past, send_email, remove_leading_space, send_contact_us_email


def get_event_image(event):
    if event.image and validate_image_url(event.image.url):
        image_url = event.image.url
    else:
        image_url = "https://res.cloudinary.com/stipaxa/image/upload/v1736449375/Woofspot/image_coming_soon_3.webp"

    return image_url


def query_all_events(request):
    try:
        events = WoofspotEvent.objects.all()
        return events
    except DatabaseError as db_error:
        messages.error(request, "A database error occurred while retrieving events. Please try again later.")
        return False
    except Exception as e:
        messages.error(request, f"An unexpected error occurred: {str(e)}")
        return False
        

def query_all_events_for_user(request, user):
    try:
        # Avoid redundant queries
        events = WoofspotEvent.objects.filter(Q(organizer=user) | Q(attendees=user)).distinct()
        return events
    except DatabaseError as db_error:
        messages.error(request, "A database error occurred while retrieving events. Please try again later.")
        return False
    except Exception as e:
        messages.error(request, f"An unexpected error occurred: {str(e)}")
        return False


def all_events_list(request):
    today = date.today()

    events = query_all_events(request)
    future_events = list(filter(lambda e: e.date > today, events))
    past_events = list(filter(lambda e: e.date <= today, events))

    for events in (future_events, past_events):
        for event in events:
            event.image_url = get_event_image(event)
            event.is_past = is_in_the_past(event.date)
            event.is_user_attendee = (request.user in event.attendees.all())
            event.average_rating = Rating.get_average_rating(event)

    next = request.GET.get("next", reverse("home"))

    return render(request, "event_app/all_events_list.html", {
        "future_events": future_events,
        "past_events": past_events,
        "next": next,
    })


def carousel_events_contact_us(request):
    # Carousel section
    tomorrow = date.today() + timedelta(days=1)
    four_weeks = tomorrow + timedelta(days=1, weeks=4)

    events = query_all_events(request)
    carousel_events = list(filter(lambda e: tomorrow <= e.date <= four_weeks, events))

    for event in carousel_events:
        event.image_url = get_event_image(event)
        event.is_past = is_in_the_past(event.date)
        event.is_user_attendee = (request.user in event.attendees.all())
        event.average_rating = Rating.get_average_rating(event)

    # Contact Us section

    # Handle submit (POST)
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            comment = form.cleaned_data["comment"]

            try:
                send_contact_us_email(name, email, comment)
                
                messages.success(request, "Your message has been sent successfully!")
                return redirect(reverse('home'))
            except ValidationError as e:
                form.add_error(None, e.messages)
                return render(request, "event_app/index.html", {
                    "events": carousel_events,
                    "form": form,
                    "scroll_to": "contact-us-section"})
        else:
            form.add_error(None, "please make changes.")
            return render(request, "event_app/index.html", {
                    "events": carousel_events,
                    "form": form,
                    "scroll_to": "contact-us-section"})

    # Handle page (GET)
    form = ContactUsForm()
    return render(request, "event_app/index.html", {
        "events": carousel_events,
        "form": form
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


@login_required
def my_event_list(request):
    today = date.today()

    events = query_all_events_for_user(request, request.user)

    hosted_by_me_future_events = list(filter(lambda e: e.organizer == request.user and e.date > today, events))
    planning_to_attend_events = list(filter(lambda e: request.user in e.attendees.all() and e.date > today, events))
    past_attending_events = list(filter(lambda e: request.user in e.attendees.all() and e.date <= today, events))
    past_organizing_events = list(filter(lambda e: e.organizer == request.user and e.date <= today, events))

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
                 {"user": request.user,
                  "hosted_by_me_future_events": hosted_by_me_future_events,
                  "planning_to_attend_events": planning_to_attend_events,
                  "past_events": past_events,
                 })


@login_required
def reservation_submit(request, slug):
    event = get_object_or_404(WoofspotEvent, slug=slug)

    if request.method == "POST" and "reserve_spot" in request.POST:
        if request.user in event.attendees.all():
            messages.error(request, "You have already reserved a spot for this event.")
        else:
            event.attendees.add(request.user)
            messages.success(request, "Slot is reserved!")
            action = "Reservation Confirmed"
            send_email(request.user, event, action)

    return redirect(reverse("event_view", args=[slug]))


@login_required
def reservation_cancel(request, slug):
    event = get_object_or_404(WoofspotEvent, slug=slug)
    next = request.GET.get("next", reverse("my_event_list"))

    if request.method == "POST" and "cancel_reservation" in request.POST:  
        event.attendees.remove(request.user)
        action = "Reservation Cancelled"
        send_email(request.user, event, action)

        messages.success(request, "Slot is canceled!")

        return redirect(reverse("my_event_list"))
        
    return render(request, "event_app/reservation_cancel.html",
    {
        "event": event,
        "user": request.user,
        "next": next
    })


def event_search_results(request):
    search_results = WoofspotEvent.objects.none()
    print(f"SEARCH_RESULTS: {search_results}")

    search_type = request.GET.get("search_type", "all")
    if search_type == "my" and not request.user.is_authenticated:
        return redirect(reverse("account_login"))

    query = request.GET.get("query", "").strip()

    if query:
        search_results = query_all_events(request)
        if search_type == "my" and request.user.is_authenticated:
            search_results = query_all_events_for_user(request, request.user)
        search_results = list(filter(lambda e: query.lower() in e.title.lower() or 
                            query.lower() in e.description.lower(), 
                            search_results))
    else:
        messages.error(request, "Please try a different search.")

    next = request.GET.get("next", "/")

    for event in search_results:
        event.image_url = get_event_image(event)
        event.is_past = is_in_the_past(event.date)
        event.is_user_attendee = (request.user in event.attendees.all())
        event.average_rating = Rating.get_average_rating(event)

    return render(
        request,
        "event_app/event_search_results.html",
        {
            "next": next,
            "query": query,
            "search_results": search_results,
            "search_type": search_type,
        },
    )


@login_required
def like_toggle(request, slug):
    event = get_object_or_404(WoofspotEvent, slug=slug)
    event.like_toggle(request.user)
    
    next = request.GET.get("next", "home")

    return render(request, "like_container.html", {
        "next": next,
        "event": event
    })


@login_required
def event_create(request):
    next = request.GET.get("next", reverse("my_event_list"))

    # Handle submit (POST)
    if request.method == "POST":
        form = EventOrganizerForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)

            event.organizer = request.user

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
                send_email(request.user, event, action)
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
                    send_email(request.user, updated_event, action)
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
    next = request.GET.get("next", reverse("my_event_list"))

    if event.organizer != request.user:
        return HttpResponseForbidden("Unauthorized access")
    
    if request.method == "POST" and "event_delete" in request.POST:
        # Delete related ratings
        Rating.objects.filter(event=event).delete()
        action = "Event Cancelled"
        send_email(request.user, event, action)
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