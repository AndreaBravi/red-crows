from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^base/', include('framework.urls', namespace="base")),
    url(r'^polls/', include('framework.polls_urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)