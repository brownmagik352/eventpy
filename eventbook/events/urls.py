from django.conf.urls import patterns, url

from events import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^events/(?P<event_id>\d+)/$', views.eventdetail, name='eventdetail'),
	url(r'^groups/(?P<group_id>\d+)/$', views.groupdetail, name='groupdetail'),
	url(r'^groups/(?P<group_id>\d+)/new/$', views.newevent, name='newevent'),

)