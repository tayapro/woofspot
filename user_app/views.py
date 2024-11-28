from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from event_app.models import WoofspotEvent

def my_signin_page(request):
    next = request.GET.get('next', '/')
    return render(request, "user_app/my_signin.html", 
    {
        "next": next,
    })


def my_signup_page(request):
    next = request.GET.get('next', '/')
    return render(request, "user_app/my_signup.html", 
    {
        "next": next,
    })


def profile_page(request):
    user = request.user
    if not user.is_authenticated:
        return redirect(reverse('my_signin'))
    next = request.GET.get('next', '/')

    if request.method == "POST":
        new_email = request.POST.get("email", "").strip()

        if new_email:
            user.email = new_email
            user.save()
            messages.success(request, "Your email address has been updated successfully!")
            return redirect(reverse('profile'))
        else:
            messages.error(request, "Please provide a valid email address.")

    latest_message = get_latest_message(request)

    return render(request, "user_app/profile.html", 
    {
        "next": next,
        "user": user,
        "latest_message": latest_message,
    })


def events_page(request):
    user = request.user
    if not user.is_authenticated:
        return redirect(reverse('my_signin'))
    events = WoofspotEvent.objects.filter(attendees=request.user) 

    if request.method == 'POST' and 'cancel_reservation' in request.POST:  
        event_id = request.POST.get('event_id')
        try:
            event = get_object_or_404(WoofspotEvent, pk=event_id)
            event.attendees.remove(request.user)
            messages.success(request, f"Your reservation for {event.title} has been cancelled.")

        except (WoofspotEvent.DoesNotExist, EventAttendance.DoesNotExist):
            messages.error(request, "There was a problem cancelling your reservation.")

    # TODO: move to try/catch
    latest_message = get_latest_message(request)

    return render(request, "user_app/events.html",
    {
        "user": user,
        "events": events,
        "latest_message": latest_message,
    })


def my_signout_page(request):
    return render(request, "user_app/my_signout.html")


def get_latest_message(request):
    all_messages = list(messages.get_messages(request))
    latest_message = all_messages[-1] if all_messages else None

    return latest_message