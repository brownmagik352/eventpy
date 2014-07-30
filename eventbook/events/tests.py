from django.test import TestCase
from events.models import Event, Group
from django.core.urlresolvers import reverse

class EventMethodTests(TestCase):

	def test_is_popular_with_not_popular(self):
		# should return false when less than 3 likes
		unpopular = Event(likes=1)
		self.assertEqual(unpopular.is_popular(), False)

	def test_is_popular_with_popular(self):
		# should return True when 3 or more likes
		pop = Event(likes=3)
		self.assertEqual(pop.is_popular(), True)

class GroupTemplateTests(TestCase):

	def test_index_view_with_no_groups(self):
		# No Groups
		response = self.client.get(reverse('events:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "<p>There are currently no registered groups.</p>", html=True)

	def test_index_view_with_one_group(self):
		# One group created
		Group.objects.create(name="Sigma Chi", numMembers = 50, private=True)
		response = self.client.get(reverse('events:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "<a href='/events/groups/1/'>Sigma Chi</a>", html=True)