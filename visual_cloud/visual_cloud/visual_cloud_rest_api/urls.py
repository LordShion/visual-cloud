from django.conf.urls import patterns, include, url
from django.contrib import admin

namespace = 'visual_cloud_rest_api'

urlpatterns = patterns('',
	#url(r'^$','visual_cloud.visual_cloud_rest_api.views.home', name='visual_cloud.visual_cloud_rest_api.home'),
	url(r'^login$','visual_cloud.visual_cloud_rest_api.views.login', name='login'),
    
)