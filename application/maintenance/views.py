from django.shortcuts import render, get_object_or_404
from .models import MaintenanceEvent, MaintenanceUpdate

# Create your views here.

def calendar_view(request):
    events = MaintenanceEvent.objects.all()
    return render(request, 'maintenance/calendar.html', {'events': events})

def maintenance_updates_view(request, event_id):
    event = get_object_or_404(MaintenanceEvent, id=event_id)
    updates = event.updates.all()
    return render(request, 'maintenance/updates.html', {'event': event, 'updates': updates})
