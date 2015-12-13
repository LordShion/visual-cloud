from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'visual_cloud_front_end/home.html')
