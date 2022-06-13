from django.shortcuts import  render, redirect
from .models import sensorList, sensor1
# Create your views here.

def index(request):
	longList = []
	latList  = []
	results = sensorList.objects.all()
	if request.method == "POST" and 'sensorID' in request.POST:
		sID = request.POST.get('sensorID', '')
		results = sensorList.objects.filter(sensorID = sID) 
		for x in results:
			longList.append(x.longitude)
			latList.append(x.latitude)
		lLength = len(longList)
		
		context = 	{	'results': results,
						'longList': longList,
						'latList': latList,
						'lLength': lLength,
					}
		return render(request, 'airMonitor/index.html', context)

	for x in results:
		longList.append(x.longitude)
		latList.append(x.latitude)
	lLength = len(longList)

	context = 	{	'results': results,
					'longList': longList,
					'latList': latList,
					'lLength': lLength,
			  	}
	return render(request, 'airMonitor/index.html', context)

def sensor(request):
	if request.method == "POST":
		results = sensor1.objects.all() 
		return render(request, 'airMonitor/sensor.html', {'results': results})
	return render(request, 'airMonitor/sensor.html')

def listPage(request):
	if request.method == "POST" and 'sensorID' in request.POST:
		criteria = request.POST.get('criteria', '')
		searchType = request.POST.get('searchType','')
		print(criteria, searchType)
		if searchType == "sensorID":
			sensors = sensorList.objects.filter(sensorID = criteria) 
		elif searchType == "longitude":
			sensors = sensorList.objects.filter(longitude = criteria) 
		elif searchType == "latitude":
			sensors = sensorList.objects.filter(latitude = criteria) 
		elif searchType == "installDate":
			sensors = sensorList.objects.filter(installDate = criteria) 
		else:
			sensors = sensorList.objects.all()

		return render(request, 'airMonitor/sensorListPage.html', {'sensors' : sensors})	
	sensors = sensorList.objects.all()
	return render(request, 'airMonitor/sensorListPage.html', {'sensors' : sensors})

def comparisons(request):
	sensors = sensorList.objects.all()
	if request.method == "POST":
		s1 = request.POST.get('sensor1','')
		s2 = request.POST.get('sensor2','')
		sList1 = sensorList.objects.get(sensorID=s1)
		sList2 = sensorList.objects.get(sensorID=s2)
		context = 	{	'sensors' : sensors,
						'sList1' : sList1,
						'sList2' : sList2,
					}
		return render(request, 'airMonitor/comparisons.html', context)	
	return render(request, 'airMonitor/comparisons.html', {'sensors' : sensors})	