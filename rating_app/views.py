from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .models import Rating
from .forms import RatingForm
from event_app.models import WoofspotEvent


def rate_create_old(request, slug):
    event = get_object_or_404(WoofspotEvent, slug=slug)

    if request.method == 'POST':
        form = RatingForm(request.POST, event=event)
        if form.is_valid():
            try:
                form.save(user=request.user)
                return redirect("event-app:event_view", slug=event.slug)
            except IntegrityError:
                form.add_error(None, "You have already rated this event.")
                return render(request, "rate_event.html", {"form": form, "event": event})
        else:
            render(request, "rate_event.html", {"form": form, "event": event})

    form = RatingForm(event=event)
    return render(request, "rate_event.html", {"form": form, "event": event})



def rate_create(request, slug):
    event = get_object_or_404(WoofspotEvent, slug=slug)
    form = RatingForm(event=event)

    if request.method == 'POST':
        form = RatingForm(request.POST, event=event)
        if form.is_valid():
            try:
                form.save(user=request.user)
                return redirect("event_view", slug=event.slug)
            except IntegrityError:
                form.add_error(None, "You have already rated this event.")
        
    return render(request, "rate_event.html", {"form": form, "event": event})