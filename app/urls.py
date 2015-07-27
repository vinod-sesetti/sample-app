from django.conf.urls import *


urlpatterns = patterns('app.views',
    url(r'^upload/$', 'upload', name='upload'),
    url(r'^$', 'userform', name='userform'), # this maps the url to views function
    url(r'^images/$', 'images', name='images')
)