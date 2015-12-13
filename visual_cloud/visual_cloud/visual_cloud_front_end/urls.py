from django.conf.urls import *

urlpatterns = patterns('',
		url(r'^$','visual_cloud.visual_cloud_front_end.views.home', name='visualcloudfrontend.home'),
)