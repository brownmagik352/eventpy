from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from django.core.urlresolvers import reverse

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
	e = group.event_set.create(title=request.POST['title'], location=request.POST['location'], time=datetime.now(), description=request.POST['description']) #likes is defaulted
	e.save()
	# return render(request, 'events/groupdetail.html', {'group':group})
	return HttpResponseRedirect(reverse('events:groupdetail', args=(group.id,)))

def like(requst, event_id):
	event = get_object_or_404(Event, pk=event_id)
	event.likes += 1
	event.save()
	return HttpResponseRedirect(reverse('events:eventdetail', args=(event.id,)))


