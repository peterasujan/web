from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^about/$',  TemplateView.as_view(template_name='website/about.html')),
    url(r'^browse/$', TemplateView.as_view(template_name='website/browse.html')),
    url(r'^login/$',  TemplateView.as_view(template_name='website/login.html')),
    url(r'^forgot/$', TemplateView.as_view(template_name='website/forgot.html')),
    url(r'^signup/$', TemplateView.as_view(template_name='website/signup.html')),
    url(r'^forgot/$', TemplateView.as_view(template_name='website/forgot.html')),
    url(r'^newAccount/$', TemplateView.as_view(template_name='website/newAccount.html')),
    url(r'^retrieve/$', TemplateView.as_view(template_name='website/retrieve.html')),
)
