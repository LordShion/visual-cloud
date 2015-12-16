import requests
import json
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST, require_GET
from visual_cloud.visual_cloud_rest_api.views import login
# Create your views here.
def home(request):

    if request.method == "GET":
            print("home")
            logged = False
            if 'connection' in request.session.keys():
                print "connection is in request"
                logged = True

            else:
                print "connection is not in request"

    if request.method == "POST":
            print "login front"
            response = login(request) 
            print response
            print("home")
            logged = response

    return render(request, 'visual_cloud_front_end/home.html',{'logged':logged})

def logout(request):
    if 'connection' in request.session.keys():
        request.session.pop("connection", None)
    return redirect(reverse('visual_cloud_front_end:home'))

