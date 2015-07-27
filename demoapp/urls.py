from django.conf.urls import patterns, url

from demoapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^create/$', 'demoapp.views.create_note', name='create'),
)