from django.conf.urls import url
from videos.views import VideoCreateView, VideoListView, VideoDetailView, VideoUpdateView, VideoDeleteView

urlpatterns = [

    url(r'^create/$', VideoCreateView.as_view(), name='create'),
    url(r'^$', VideoListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', VideoDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', VideoUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', VideoDeleteView.as_view(), name='delete'),

]
