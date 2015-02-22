from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import framework.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', framework.views.index, name='index'),
    url(r'^db', framework.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

)
