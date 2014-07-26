from django.shortcuts import render
from django.http import HttpResponse
from models import Event

def index(request):
	message = ""
	for e in Event.objects.all():
		message += "%s\t" % e.title
	return HttpResponse("All Events:\t" + message)

def detail(request, event_id):
	e = Event.objects.get(pk=event_id)
	return HttpResponse("%s" % e.title)