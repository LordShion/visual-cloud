#-*- coding:utf-8 -*-
"""visual_cloud URL Configuration

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
from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    #path(r'^admin/$', admin.site.urls),

    path(r'', include(('visual_cloud_front_end.urls', 'visual_cloud_front_end'), namespace='visual_cloud_front_end')),
    path(r'rest/', include(('visual_cloud_rest_api.urls', 'visual_cloud_rest_api'), namespace='visual_cloud_rest_api'))
]
