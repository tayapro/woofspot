from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

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

    all_messages = list(messages.get_messages(request))
    latest_message = all_messages[-1] if all_messages else None

    if request.method == "POST":
        new_email = request.POST.get("email", "").strip()

        if new_email:
            user.email = new_email
            user.save()
            messages.success(request, "Your email address has been updated successfully!")
            return redirect(reverse('profile'))
        else:
            messages.error(request, "Please provide a valid email address.")

    return render(request, "user_app/profile.html", 
    {
        "next": next,
        "user": user,
        "latest_message": latest_message,
    })


def my_signout_page(request):
    return render(request, "user_app/my_signout.html")