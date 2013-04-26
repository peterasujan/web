from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^authenticate/$', 'auth.views.auth_user'),
    url(r'^verify/$', 'auth.views.auth_verify'),
)
