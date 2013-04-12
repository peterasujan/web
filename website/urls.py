from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
    url(r'^about/$', direct_to_template, {'template' : 'website/about.html'}),
    url(r'^browse/$', direct_to_template, {'template' : 'website/browse.html'}),
    url(r'^login/$', direct_to_template, {'template' : 'website/login.html'}),
    url(r'^forgot/$', direct_to_template, {'template' : 'website/forgot.html'}),
    url(r'^signup/$', direct_to_template, {'template' : 'website/signup.html'}),
)
