from django.urls import path
from django.contrib import admin
from . import views

# namespace = 'rest'

urlpatterns = [
	path(r'admin/', admin.site.urls),
	path(r'login/', views.login, name='login')
]