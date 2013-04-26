from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    url(r'^authenticate/$', 'auth.views.auth_user'),
    url(r'^verify/$', 'auth.views.auth_verify'),
)
