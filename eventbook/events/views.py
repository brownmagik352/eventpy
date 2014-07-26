from django.shortcuts import render, get_object_or_404

from events.models import Event

def index(request):
	events = Event.objects.all()
	context = {'events':events}
	return render(request, 'events/index.html', context)

def detail(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	return render(request, 'events/detail.html', {'event':event})