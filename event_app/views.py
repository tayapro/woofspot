from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from .models import WoofspotEvent
from .forms import EventOrganizerForm


class FetchEvents(generic.ListView):
    queryset = WoofspotEvent.objects.all()
    template_name = "index.html"
    context_object_name = "events"
    paginate_by = 6


def event_view(request, slug):
    event = get_object_or_404(WoofspotEvent, slug=slug)

    if request.method == 'POST' and 'reserve_spot' in request.POST:
        if request.user.is_authenticated:
            if request.user in event.attendees.all():
                messages.error(request, "You have already reserved a spot for this event.")
            else:
                event.attendees.add(request.user)
                messages.success(request, "Slot is reserved!")
        else:
            return redirect(f"{reverse('signin')}?next={request.path}")

    user_registered = (
        request.user.is_authenticated and request.user in event.attendees.all()
    )
    return render(request, "event_view.html", 
                 {"event": event, 
                 "user_registered": user_registered}
                 )


def my_event_list(request):
    user = request.user
    if not user.is_authenticated:
        return redirect(reverse('account_login'))
    
    attending_events = WoofspotEvent.objects.filter(attendees=request.user)
    organizing_events = WoofspotEvent.objects.filter(organizer=request.user)

    return render(request, "my_event_list.html",
    {
        "user": user,
        "attending_events": attending_events,
        "organizing_events": organizing_events
    })


def reservation_cancel(request, slug):
    user = request.user
    if not user.is_authenticated:
        return redirect(reverse('account_login'))

    event = get_object_or_404(WoofspotEvent, slug=slug)

    if request.method == 'POST' and 'cancel_reservation' in request.POST:  
        event.attendees.remove(request.user)
        return redirect(reverse('my_event_list'))
        
    return render(request, "reservation_cancel.html",
    {
        "event": event,
        "user": user,
    })


def event_search_results(request):
    query = request.GET.get('query')  
    results = []
    if query:
        results = WoofspotEvent.objects.filter(
            Q(title__icontains=query) |  
            Q(content__icontains=query)  
        )
    next = request.GET.get('next', "/")

    return render(request,
                  "event_search_results.html", 
                  {
                    "next": next,
                    "query": query, 
                    "results": results
                  })


def my_event_search_results(request):
    user = request.user
    if not user.is_authenticated:
        return redirect(reverse('account_login'))
    
    events = WoofspotEvent.objects.filter(
        Q(attendees=user) | Q(organizer=user)
    )
    
    query = request.GET.get('query')  
    results = events
    if query:
        results = results.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    
    next = request.GET.get('next', "/my/event/list/")
    
    return render(request, 
                  "event_search_results.html",
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
    # Handle submit (POST)
    if request.method == "POST":
        form = EventOrganizerForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect("my_event_list")
        else:
            return render(request, "event_create.html", {"form": form })

    # Handle page (GET)
    form = EventOrganizerForm()
    return render(request, "event_create.html", {"form": form })


@login_required
def event_edit(request, slug):
    event = get_object_or_404(WoofspotEvent, slug=slug)
    if event.organizer != request.user:
        return HttpResponseForbidden("Unauthorized access")
    # Handle submit (POST)
    if request.method == "POST":
        form = EventOrganizerForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect("my_event_list")
        else:
            return render(request, "event_edit.html", {"form": form, "event": event })

    # Handle page (GET)
    form = EventOrganizerForm(instance=event)
    return render(request, "event_edit.html", {"form": form, "event": event })


@login_required
def event_delete(request, slug):
    event = get_object_or_404(WoofspotEvent, slug=slug)
    if event.organizer != request.user:
        return HttpResponseForbidden("Unauthorized access")
    event.delete()
    return redirect("events")

