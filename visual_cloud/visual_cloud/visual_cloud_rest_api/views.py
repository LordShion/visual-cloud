import types
from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

# Create your views here.
@require_POST
def login(request):
    print "connecting......................."
    cls = get_driver(Provider.OUTSCALE_INC)
    driver = cls(request.POST.get("login_ak"), request.POST.get("login_sk"),region=request.POST.get("login_region"))
    images = None
    try:
        images = driver.list_images()
    except:
        print "error connecting" 
    if isinstance(images,types.ListType):
        # login ak sk and region are okay API is responding
        request.session['connection'] = {
            'login_ak': request.POST.get("login_ak"),
            'login_sk': request.POST.get("login_sk"),
            'login_region': request.POST.get("login_region"),

        }
        return True

 # render(request, 'visual_cloud_front_end:home',{'logged':True})
    else:
        print "problem with connection"
        request.session.pop("connection", None)
        # return redirect(reverse('visual_cloud_front_end:home'), {'logged':False, 'error':'problem with connection'})
        return False

