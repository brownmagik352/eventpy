from django.db import models
from datetime import datetime

class Group(models.Model):
	name = models.CharField(max_length=75, unique=True)
	numMembers = models.IntegerField(default=0)
	private = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name

class Event(models.Model):
	group = models.ForeignKey(Group, null=True)
	title = models.CharField(max_length = 100, unique = True)
	location = models.CharField(max_length=50)
	time = models.DateTimeField(default=datetime.now())
	description =models.TextField(max_length=500)
	likes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

	def is_popular(self):
		return self.likes >=3


