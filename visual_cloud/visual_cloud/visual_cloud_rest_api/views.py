from django.shortcuts import render
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

# Create your views here.
def login(request):

    sizes = 0
    images = 0

    cls = get_driver(Provider.OUTSCALE_INC)
    driver = cls(request.POST.get("login_ak"), request.POST.get("login_sk"),region=request.POST.get("login_region"))

    sizes = driver.list_sizes()
    images = driver.list_images()

    print sizes
    print images

    return render(request, 'visual_cloud_rest_api/login.html')
