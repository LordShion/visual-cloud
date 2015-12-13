from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$','visual_cloud.visual_cloud_rest_api.views.home', name='home'),
    
)