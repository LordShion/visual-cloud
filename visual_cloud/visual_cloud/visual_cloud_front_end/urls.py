from django.conf.urls import *

# namespace = 'front'

urlpatterns = patterns('',
		url(r'^$','visual_cloud.visual_cloud_front_end.views.home', name='home'),
		url(r'^logout$','visual_cloud.visual_cloud_front_end.views.logout', name='logout'),
)