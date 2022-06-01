from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'airMonitor/index.html')

def sensor(request):
	return render(request, 'airMonitor/sensor.html')

def sensorList(request):
	return render(request, 'airMonitor/sensorList.html')

def comparisons(request):
	return render(request, 'airMonitor/comparisons.html')	