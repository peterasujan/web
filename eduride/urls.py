from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import website


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eduride.views.home', name='home'),
    # url(r'^eduride/', include('eduride.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='website/index.html')),
    url(r'^w/', include('website.urls')),
    url(r'^log/$', 'log.views.save_log'),
    url(r'^auth/', include('auth.urls')),
    url(r'^mvle/$', 'mvle.views.process_mvle'),
    url(r'^assignment/$', 'assignment.views.assignment_list'),
)
