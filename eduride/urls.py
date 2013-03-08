from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
import website


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eduride.views.home', name='home'),
    # url(r'^eduride/', include('eduride.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', direct_to_template, {'template' : 'website/index.html'}),
    url(r'^w/', include('website.urls')),
    url(r'^l/', include('log.urls')),
)
