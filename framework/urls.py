from django.conf.urls import patterns, url

from framework import views

urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),	
    url(r'^artist/(?P<pk>\w+)/$', views.MusicianView.as_view(), name='musician'),    
    url(r'^reviewer/(?P<pk>\w+)/$', views.ReviewerView.as_view(), name='reviewer'),
    url(r'^review/(?P<pk>\w+)/$', views.ReviewView.as_view(), name='review'),
    url(r'^music/(?P<pk>\w+)/$', views.MusicView.as_view(), name='music'),

    url(r'^create/artist/$', views.CreateMusicianView.as_view(), name='createmusician'),
    url(r'^create/reviewer/$', views.CreateReviewerView.as_view(), name='createreviewer'),
    url(r'^add/music/$', views.CreateMusicView.as_view(), name='createmusic'),
    url(r'^add/review/$', views.CreateReviewView.as_view(), name='createreview'),

    url(r'^create/artist/thanks/$', views.ThanksView.as_view(), name='thanksmusician'),
    url(r'^create/reviewer/thanks/$', views.ThanksView.as_view(), name='thanksreviewer'),

    url(r'^artists/$', views.ListMusicianView.as_view(), name='listmusician'),
    url(r'^reviewers/$', views.ListReviewerView.as_view(), name='listreviewer'),
    url(r'^reviews/$', views.ListReviewView.as_view(), name='listreview'),
    url(r'^music/$', views.ListMusicView.as_view(), name='listmusic'),
)
