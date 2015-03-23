from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'myapp.views.index'),
    url(r'^hello/(?P<name>[\w+\s])?', 'myapp.views.index'),
)
