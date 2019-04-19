from django.conf.urls import url
from music.views import index,detail,favorite

app_name='music'

urlpatterns = [
    #/music/
    url(r'^$',index,name='index'),

    #/music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', detail,name='detail'),

    #/music/<album_id>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', favorite,name='favorite'),

#in regex ^ represents start and $ represents the end of expression
]
