from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, EventRegistration
from .forms import EventForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.http import HttpResponse


# Check if user is admin
def is_admin(user):
    return user.is_superuser


# List all events
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


# Event details
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})


# Create a new event
@user_passes_test(is_admin)
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_form.html', {'form': form})


# Edit an event
@user_passes_test(is_admin)
def event_edit(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/event_form.html', {'form': form})


# Delete an event
@user_passes_test(is_admin)
def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})


# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('event_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("event_list")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")


# Register for an event
@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    user = request.user

    if EventRegistration.objects.filter(user=user, event=event).exists():
        messages.warning(request, "You have already registered for this event.")
        return redirect('event_detail', event_id=event.id)

    EventRegistration.objects.create(user=user, event=event)
    messages.success(request, "Successfully registered for the event!")

    return redirect('event_detail', event_id=event.id)


# User profile
@login_required
def user_profile(request):
    registrations = EventRegistration.objects.filter(user=request.user)
    return render(request, 'events/user_profile.html', {'registrations': registrations})


# Home page
@login_required
def home(request):
    return render(request, 'events/home.html', {'user': request.user})



#  Home page
def index(request):
    return HttpResponse("<h1>Welcome to College Events 🎉</h1><p>This is your homepage.</p>")


# Add event page (optional)
def add_event(request):
    return HttpResponse("<h1>Add a new event here.</h1>")