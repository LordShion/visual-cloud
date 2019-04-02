import requests
import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST, require_GET
from visual_cloud.visual_cloud_rest_api.views import login
from visual_cloud.visual_cloud_front_end import forms


#  Create your views here.
def home(request):
    formlogin = None
    error = None
    if request.method == "GET":
            print("home")
            logged = False
            if hasattr(request, 'session'):
                if 'connection' in request.session.keys():
                    print("connection is in request")
                    logged = True

                else:
                    print("connection is not in request")
                    formlogin = forms.LoginForm
            else:
                formlogin = forms.LoginForm

    if request.method == "POST":
        print("login front")
        response = login(request) 
        print(response)
        print("home")
        logged = response
        if not logged:
            formlogin = forms.LoginForm(request.POST)
            error = 'problem with connection'

    return render(request, 'visual_cloud_front_end/home.html',{'logged':logged , 'formlogin': formlogin, 'error':error })

def logout(request):
    if 'connection' in request.session.keys():
        request.session.pop("connection", None)
    return redirect(reverse('visual_cloud_front_end:home'))

