from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm

@login_required
def event_list(request):
    events = Event.objects.filter(user=request.user)  # Show only user’s events
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user  # Assign event to logged-in user
            event.save()
            return redirect('event_list')
    else:
        # Pre-fill the form if a date is passed from FullCalendar
        date = request.GET.get('date', None)
        form = EventForm(initial={'date': date})
        
    return render(request, 'events/event_form.html', {'form': form})

import json

@login_required
def event_update(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # ✅ Redirects back to event list page
    
    else:
        form = EventForm(instance=event)
    
    return render(request, 'events/event_form.html', {'form': form})  # ✅ Renders the edit form on a new page


@login_required
def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    
    if request.method == "POST":
        event.delete()
        return redirect('event_list')
    
    return render(request, 'events/event_confirm_delete.html', {'event': event})


from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            login(request, user)  # Log in after registration
            return redirect('event_list')  # Redirect to events page
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

from django.http import JsonResponse

from django.http import JsonResponse

@login_required
def event_api(request):
    events = Event.objects.filter(user=request.user)
    event_list = []
    
    for event in events:
        event_list.append({
            'id': event.id,
            'title': event.title,
            'start': str(event.date),
            'color': event.color,  # ✅ Add color to API response
            'extendedProps': {
                'time': str(event.time),
                'priority': event.priority,
                'notes': event.notes,
            }
        })
    
    return JsonResponse(event_list, safe=False)

from django.http import JsonResponse
import json

@login_required
def update_event_date(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)

    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))  # Parse JSON request
            new_date = data.get('date')  # Get the new date from request
            if new_date:
                event.date = new_date
                event.save()
                return JsonResponse({'success': True})  # ✅ Update successful
            else:
                return JsonResponse({'success': False, 'error': 'Invalid date'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)