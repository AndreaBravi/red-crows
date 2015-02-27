from django.conf.urls import patterns, url

from framework import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView2.as_view(), name='index'),
    url(r'^(?P<pk>\w+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\w+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<poll_id>\w+)/vote/$', views.vote, name='vote'),
)