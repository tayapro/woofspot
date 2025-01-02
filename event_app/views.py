from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.db import IntegrityError
from django.utils.timezone import now
from django.core.mail import EmailMessage, get_connection, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import WoofspotEvent
from .forms import EventOrganizerForm
from .models import Rating
from .forms import ReviewForm

TODAY = now().date()


def event_list(request):
    events = WoofspotEvent.objects.filter(event_date__gt=TODAY)

    return render(request, "event_app/index.html", {
        "events": events,
    })


def event_view(request, slug):
    event = get_object_or_404(WoofspotEvent, slug=slug)
    average_rating = Rating.get_average_rating(event)
    user_registered = (
        request.user.is_authenticated and request.user in event.attendees.all()
    )

    next = request.GET.get("next", "/")

    return render(
        request,
        "event_app/event_view.html",
        {
            "event": event,
            "next": next,
            "today": TODAY,
            "user_registered": user_registered,
            "average_rating": average_rating,
        },
    )


def my_event_list(request):
    user = request.user
    if not user.is_authenticated:
        return redirect(reverse("account_login"))
    
    future_organizing_events = WoofspotEvent.objects.filter(
                                organizer=request.user,
                                event_date__gt=TODAY)
    future_attending_events = WoofspotEvent.objects.filter(
                                attendees=request.user,
                                event_date__gt=TODAY)
    past_attending_events = WoofspotEvent.objects.filter(
                                attendees=request.user,
                                event_date__lte=TODAY)
    past_organizing_events = WoofspotEvent.objects.filter(
                                organizer=request.user,
                                event_date__lte=TODAY)
    past_events = WoofspotEvent.objects.filter(
            Q(organizer=request.user, event_date__lte=TODAY) |  
            Q(attendees=request.user, event_date__lte=TODAY))

    return render(request, "event_app/my_event_list.html",
                 {"user": user,
                  "future_organizing_events": future_organizing_events,
                  "future_attending_events": future_attending_events,
                  "past_events": past_events,
                 })


def send_email(user, event, action):
    with get_connection(host=settings.EMAIL_HOST, 
            port=settings.EMAIL_PORT,  
            username=settings.EMAIL_HOST_USER, 
            password=settings.EMAIL_HOST_PASSWORD, 
            use_tls=settings.EMAIL_USE_TLS
        ) as connection:  
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [user.email, ]

        context = {'user': user, 'event': event}

        subject = f"{action}: {event.title}"
        if action == "Event Created":
            text_content = render_to_string('event_app/emails/event_created.txt', context)
            html_content = render_to_string('event_app/emails/event_created.html', context)

            email = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send()
        elif action == "Event Cancelled":
            attendees = event.attendees.all()
            recipient_list = [attendee.email for attendee in attendees]
            text_content = render_to_string('event_app/emails/event_cancelled.txt', context)
            html_content = render_to_string('event_app/emails/event_cancelled.html', context)
            
            email = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send()
        elif action == "Reservation Confirmed":
            text_content = render_to_string('event_app/emails/reservation_confirmed.txt', context)
            html_content = render_to_string('event_app/emails/reservation_confirmed.html', context)

            email = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send()
        elif action == "Reservation Cancelled":
            text_content = render_to_string('event_app/emails/reservation_cancelled.txt', context)
            html_content = render_to_string('event_app/emails/reservation_cancelled.html', context)

            email = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
            email.attach_alternative(html_content, "text/html")
            email.send()
        elif action == "Some Changes about your Event":
            attendees = event.attendees.all()
            recipient_list = [attendee for attendee in attendees] + [event.organizer]

            for recipient in recipient_list:
                context = {
                    'user': recipient,
                    'event': event,
                }
        
                text_content = render_to_string('event_app/emails/event_changed.txt', context)
                html_content = render_to_string('event_app/emails/event_changed.html', context)

                email = EmailMultiAlternatives(subject, text_content, email_from, [recipient.email],)
                email.attach_alternative(html_content, "text/html")
                email.send()


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


def reservation_cancel(request, slug):
    user = request.user
    if not user.is_authenticated:
        return redirect(reverse("account_login"))

    event = get_object_or_404(WoofspotEvent, slug=slug)

    if request.method == "POST" and "cancel_reservation" in request.POST:  
        event.attendees.remove(user)
        action = "Reservation Cancelled"
        send_email(user, event, action)
        return redirect(reverse("my_event_list"))
        
    return render(request, "event_app/reservation_cancel.html",
    {
        "event": event,
        "user": user,
    })


def event_search_results(request):
    query = request.GET.get("query")  
    results = []
    if query:
        results = WoofspotEvent.objects.filter(
            Q(title__icontains=query) |  
            Q(content__icontains=query)  
        )
    next = request.GET.get("next", "/")

    return render(request,
                  "event_app/event_search_results.html", 
                  {
                    "next": next,
                    "query": query, 
                    "results": results
                  })


def my_event_search_results(request):
    user = request.user
    if not user.is_authenticated:
        return redirect(reverse("account_login"))
    
    events = WoofspotEvent.objects.filter(
        Q(attendees=user) | Q(organizer=user)
    )
    
    query = request.GET.get("query")  
    results = events
    if query:
        results = results.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    
    next = request.GET.get("next", "/my/event/list/")
    
    return render(request, 
                  "event_app/event_search_results.html",
                  {
                    "next": next,
                    "query": query,
                    "results": results
                  })


def like_toggle(request, slug):
    if not request.user.is_authenticated:
        return HttpResponseForbidden("You must be logged in to like an event.")
    
    event = get_object_or_404(WoofspotEvent, slug=slug)
    event.like_toggle(request.user)
    return render(request, "like_button.html", {
        "event": event
    })


@login_required
def event_create(request):
    user = request.user

    # Handle submit (POST)
    if request.method == "POST":
        form = EventOrganizerForm(request.POST, request.FILES)

        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            action = "Event Created"
            send_email(user, event, action)
            return redirect("my_event_list")
        else:
            return render(request, "event_app/event_create.html", {"form": form })

    # Handle page (GET)
    form = EventOrganizerForm()
    return render(request, "event_app/event_create.html", {"form": form })


@login_required
def event_edit(request, slug):
    user = request.user
    event = get_object_or_404(WoofspotEvent, slug=slug)
    if event.organizer != request.user:
        return HttpResponseForbidden("Unauthorized access")

    original_date = event.event_date
    original_event_start_time = event.event_start_time
    original_event_end_time = event.event_end_time
    
    # Handle submit (POST)
    if request.method == "POST":
        form = EventOrganizerForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            updated_event = form.save(commit=False)
            updated_event.save()

            if original_date != updated_event.event_date or original_event_start_time != updated_event.event_start_time or original_event_end_time != updated_event.event_start_time:
                
                action = "Some Changes about your Event"
                send_email(user, event, action)

            return redirect("my_event_list")
        else:
            return render(request, "event_app/event_edit.html", {"form": form, "event": event })

    # Handle page (GET)
    form = EventOrganizerForm(instance=event)
    return render(request, "event_app/event_edit.html", {"form": form, "event": event })


@login_required
def event_delete(request, slug):
    event = get_object_or_404(WoofspotEvent, slug=slug)
    user = request.user

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
    })


@login_required
def rating_submit(request, slug):
    event = get_object_or_404(WoofspotEvent, slug=slug)
    next = request.GET.get("next", "my_event_list")

    # Handle submit (POST)
    if request.method == "POST":
        form = ReviewForm(request.POST, event=event)
        if form.is_valid():
            Rating.objects.filter(user=request.user, event=event).delete()

            rating = form.save(commit=False)
            rating.user = request.user
            rating.event = event
            rating.save()

            return redirect("event_view", slug=event.slug)

        return render(request, "event_app/rating_submit.html", 
                      {"next": next, 
                      "form": form, 
                      "event": event})

    # Handle page (GET)
    form = ReviewForm(event=event)
    return render(request, "event_app/rating_submit.html", {"form": form, "event": event, "next": next})