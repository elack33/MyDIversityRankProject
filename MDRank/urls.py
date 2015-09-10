"""MDRank URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from MyDiRa import views as mdr_views
from accounts import views as accounts_views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pwd/', include('password_reset.urls')),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^create_user/$', accounts_views.create_user, name='create_user'),
    url(r'^test/$', mdr_views.test, name='test'),
    url(r'^landing/$', mdr_views.landing, name='landing'),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
    url(r'^manual_entry/$', mdr_views.manual_entry, name='manual'),
    url(r'^show_data/$', mdr_views.show_data, name='show_data'),

]
