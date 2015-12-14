from django.conf.urls import *

namespace = 'visual_cloud_front_end'

urlpatterns = patterns('',
		url(r'^$','visual_cloud.visual_cloud_front_end.views.home', name='home'),
)