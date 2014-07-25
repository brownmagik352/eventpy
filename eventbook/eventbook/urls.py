from django.conf.urls import patterns, include, url
from events import views as eviews
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventbook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', eviews.index, name="home"),
    url(r'^events/', include('events.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
