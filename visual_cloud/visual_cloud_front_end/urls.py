from django.urls import path
from . import views

urlpatterns = [
		path(r'', views.home, name='home'),
		path(r'home', views.home, name='home'),
		path(r'logout', views.logout, name='logout')
]