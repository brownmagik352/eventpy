from django.db import models

class Event(models.Model):
	title = models.CharField(max_length = 100)
	location = models.CharField(max_length=50)
	time = models.DateTimeField()
	description =models.TextField(max_length=500)

	def __unicode__(self):
		return self.title

	def isEXEvent(self):
		return (self.location == "33 Lynwood")