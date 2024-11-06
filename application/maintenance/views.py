from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.db.models import Max
from .models import MaintenanceEvent, MaintenanceUpdate

# Create your views here.
def calendar_view(request):
    now = timezone.now()

    active_events = MaintenanceEvent.objects.filter(start_time__lte=now, end_time__gte=now).prefetch_related('updates')
    upcoming_events = MaintenanceEvent.objects.filter(start_time__gt=now).prefetch_related('updates')


    for event in active_events:
        event.latest_update = event.updates.order_by('-timestamp').first()
    for event in upcoming_events:
        event.latest_update = event.updates.order_by('-timestamp').first()

    context = {
        'active_events': active_events,
        'upcoming_events': upcoming_events,
    }

    return render(request, 'maintenance/calendar.html', context)

#def calendar_view(request):
#    events = MaintenanceEvent.objects.all()
#    return render(request, 'maintenance/calendar.html', {'events': events})

def maintenance_updates_view(request, event_id):
    event = get_object_or_404(MaintenanceEvent, id=event_id)
    updates = event.updates.all()
    return render(request, 'maintenance/updates.html', {'event': event, 'updates': updates})
