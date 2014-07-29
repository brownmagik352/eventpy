from django.shortcuts import render, get_object_or_404
from datetime import datetime

from events.models import Event, Group

def index(request):
	events = Event.objects.all()
	groups = Group.objects.all()
	context = {'events':events, 'groups':groups}
	return render(request, 'events/index.html', context)

def eventdetail(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	return render(request, 'events/eventdetail.html', {'event':event})

def groupdetail(request, group_id):
	group = get_object_or_404(Group, pk=group_id)
	return render(request, 'events/groupdetail.html', {'group':group})

def newevent(request, group_id):
	group = get_object_or_404(Group, pk=group_id)
	e = group.event_set.create(title=request.POST['title'], location=request.POST['location'], time=datetime.now(), description="No description")
	e.save()
	return render(request, 'events/groupdetail.html', {'group':group})