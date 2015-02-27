from django.conf.urls import patterns, url

from framework import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<musician_id>\w+)/musician/$', views.MusicianView.as_view(), name='musician'),
    url(r'^(?P<reviewer_id>\w+)/reviewer/$', views.ReviewerView.as_view(), name='reviewer'),
    url(r'^(?P<review_id>\w+)/review/$', views.ReviewView.as_view(), name='review'),
)
