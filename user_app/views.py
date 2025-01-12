from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from event_app.models import WoofspotEvent

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import ContactUsForm

def contact_us_form_submit(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            comment = form.cleaned_data["comment"]

            send_mail(
                subject=f"Contact Form Submission from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{comment}",
                from_email=email,
                recipient_list=["woofspot.app@gmail.com"],
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            return HttpResponseRedirect(reverse("home"))
        else:
            messages.error(request, "There was an error in your submission. Please try again.")

    return render(request, "base.html", {"form": ContactUsForm()})


@login_required
def profile(request):
    user = request.user
    next = request.GET.get('next', '/')

    return render(request, "user_app/profile.html", 
    {
        "next": next,
        "user": user,
    })


@login_required
def change_email(request):
    user = request.user
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


@login_required
def change_username(request):
    if request.method == "POST":
        new_username = request.POST.get("new_username", "").strip()

        if not new_username:
            messages.error(request, "Username cannot be empty.")
            return redirect("profile")

        if request.user.username == new_username:
            messages.warning(request, "This is already your username.")
            return redirect("profile")

        # Check if the new username is already taken
        if User.objects.filter(username=new_username).exists():
            messages.error(request, "This username is already taken.")
            return redirect("profile")

        # Update username
        request.user.username = new_username
        request.user.save()

        messages.success(request, "Your username has been updated successfully!")
        return redirect("profile")

    return render(request, "profile.html")



def get_latest_message(request):
    all_messages = list(messages.get_messages(request))
    latest_message = all_messages[-1] if all_messages else None

    return latest_message