"""sample_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
admin.autodiscover()
from django.conf.urls.static import static
from django.conf import settings
# from sample_project.views import logout_page

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url (r'^$', 'sample_project.views.index', name='index'),
    #url (r'^home/', 'sample_project.views.index1', name='index1'),
    #url (r'^home/', include('sample_project.urls', namespace='home')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^accounts/', include('allauth.urls')),
    #url(r'^$', TemplateView.as_view(template_name='sample_project/index.html')),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='sample_project/profile.html')),
    url(r'^image/', include('app.urls', namespace="app")),
    #url(r'^calendar/', include('calendar_app.urls', namespace="calendar")),
    url(r'^app_calendar/', include('app_calendar.urls', namespace="app_calendar")),
    url(r'^search/', include('haystack.urls',namespace="haystack")),
    url(r'^searchitem/', include('demoapp.urls',namespace="demoapp")),
    url(r'^create/$', 'demoapp.views.create_note', name='create'),
    url(r'^todo/$', 'demoapp.views.index1', name='todo'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
