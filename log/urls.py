from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    url(r'^push/$', 'log.views.save_log'),
)
