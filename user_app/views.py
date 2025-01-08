from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from event_app.models import WoofspotEvent

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import ContactForm

def contact_form_submit(request):

    print("BLA")

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():

            print("FORM IS VALID")

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

    return render(request, "base.html", {"form": ContactForm()})


def profile(request):
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


def get_latest_message(request):
    all_messages = list(messages.get_messages(request))
    latest_message = all_messages[-1] if all_messages else None

    return latest_message