from django.shortcuts import render

# Create your views here.
def home(request):
    print("home")
    logged = False
    if not request.user.is_authenticated():
        print ("not authenticated")

        logged = False
    else: 
        print("authenticated")
        logged = True

    return render(request, 'visual_cloud_front_end/home.html',{'logged':logged})
