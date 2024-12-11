from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from event_app.models import WoofspotEvent

def my_signup_page(request):
    next = request.GET.get('next', '/')
    return render(request, "my_signup.html", 
    {
        "next": next,
    })


def profile_page(request):
    user = request.user
    if not user.is_authenticated:
        return redirect(reverse('account_login'))
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

    return render(request, "profile.html", 
    {
        "next": next,
        "user": user,
        "latest_message": latest_message,
    })


def my_signout_page(request):
    return render(request, "my_signout.html")


def get_latest_message(request):
    all_messages = list(messages.get_messages(request))
    latest_message = all_messages[-1] if all_messages else None

    return latest_message