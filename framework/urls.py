from django.conf.urls import patterns, url

from framework import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),	
    url(r'^artist/(?P<pk>\w+)/$', views.MusicianView.as_view(), name='musician'),    
    url(r'^reviewer/(?P<pk>\w+)/$', views.ReviewerView.as_view(), name='reviewer'),
    url(r'^review/(?P<pk>\w+)/$', views.ReviewView.as_view(), name='review'),
    url(r'^music/(?P<pk>\w+)/$', views.MusicianProductView.as_view(), name='musicianproduct'),

    url(r'^create/artist/$', views.CreateMusicianView.as_view(), name='createmusician'),
    url(r'^create/reviewer/$', views.CreateReviewerView.as_view(), name='createreviewer'),

    url(r'^create/artist/thanks/$', views.ThanksView.as_view(), name='thanksmusician'),
    url(r'^create/reviewer/thanks/$', views.ThanksView.as_view(), name='thanksreviewer'),
)
