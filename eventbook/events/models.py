from django.db import models
from datetime import datetime


class Event(models.Model):
	title = models.CharField(max_length = 100, unique = True)
	location = models.CharField(max_length=50)
	time = models.DateTimeField(default=datetime.now())
	description =models.TextField(max_length=500)
	likes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

	def atEXhouse(self):
		return self.location == "33 Lynwood"

	def popular(self):
		return self.likes >=3


