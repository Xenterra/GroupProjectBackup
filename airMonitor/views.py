import requests
import json
from datetime import datetime, timedelta
import pytz
from django.shortcuts import  render, redirect
from airMonitor.models import sensorList, BME280Reading, SDS011Reading, DHT22Reading, PastBME280Readings, PastDHT22Readings, PastSDS011Readings
# Create your views here.

def index(request):
	longList = []
	latList  = []
	idList = []
	if request.method == "POST" and 'sensorID' in request.POST:
		sID = request.POST.get('sensorID', '')
		sensors = sensorList.objects.filter(sensorID = sID) 
		for x in sensors:
			idList.append(x.sensorID)
			longList.append(x.longitude)
			latList.append(x.latitude)
		lLength = len(idList)

		context = 	{	'sensors'	: sensors,
						'idList' 	: idList,
						'longList'	: longList,
						'latList'	: latList,
						'lLength'	: lLength,
				  	}
		return render(request, 'airMonitor/index.html', context)

	results = sensorList.objects.all()
	for x in results:
		idList.append(x.sensorID)
		longList.append(x.longitude)
		latList.append(x.latitude)
	lLength = len(idList)

	context = 	{	'results'	: results,
					'idList' 	: idList,
					'longList'	: longList,
					'latList'	: latList,
					'lLength'	: lLength,
			  	}
	return render(request, 'airMonitor/index.html', context)

def sensor(request):
	longList = []
	latList  = []
	idList = []
	liveList=[]
	historyRange = [0,0,0,0,0,0,0]

	now = datetime.now()
	for x in range(7):
		d = now - timedelta(days=x+2)
		historyRange[x] = (str(d.strftime("%B %d, %Y")),int(d.strftime("%m")),int(d.strftime("%d")))


	if request.method == "POST":
		criteria = request.POST.get('Selection', '')
		sType = sensorList.objects.filter(sensorID = criteria)
		for x in sType:
			idList.append(x.sensorID)
			longList.append(x.longitude)
			latList.append(x.latitude)
		lLength = len(idList)

		targetLong = sType[0].longitude
		targetLat = sType[0].latitude
		url = "https://weatherapi-com.p.rapidapi.com/current.json"

		querystring = {"q":"57.106,-2.088"}

		headers = {
			"X-RapidAPI-Key": "47079ababdmshc4905f943207bedp19acf7jsn5bcb9cf62b22",
			"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers, params=querystring)
		rawLiveJSON =response.text
		liveJSON = json.loads(rawLiveJSON)

		liveTemp	= liveJSON["current"]["temp_c"]
		livePress	= liveJSON["current"]["pressure_mb"]
		liveHumi	= liveJSON["current"]["humidity"]
		liveP1		= liveJSON["current"]["wind_mph"]/2
		liveP2		= (liveJSON["current"]["wind_mph"]+1)/2
		now = datetime.now(pytz.timezone('Europe/London'))
		liveTimestamp = now.strftime("%d/%m/%Y %H:%M:%S")

		currentWeather = ""
		weatherImage = ""

		#for x in liveJSON:
		#	liveList += x
		#print(liveList)

		if sType[0].sensorType == "SDS011":
			p1List = []
			p2List = []
			labelList = []
			results = SDS011Reading.objects.filter(sensorID = criteria)
			results2 = PastSDS011Readings.objects.filter(sensorID = criteria)
			for x in results:
				p1List.append(x.P1)
				p2List.append(x.P2)
				labelList.append((x.timestamp).strftime("%d/%m/%Y, %H:%M:%S"))
			context = 	{	'results': results,
							'results2': results2,
							'p1List': p1List,
							'p2List': p2List,
							'labelList': labelList,
							'idList' : idList,
							'longList' : longList,
							'latList' : latList,
							'lLength' : lLength,
							'sType' : sType[0],
							'liveP1' : liveP1,
							'liveP2' : liveP2,
							'historyRange':historyRange,
							'liveTimestamp':liveTimestamp,
						}
			return render(request, 'airMonitor/sensor_SDS.html', context)
		elif sType[0].sensorType == "BME280":
			tempList = []
			humList = []
			pressList = []
			labelList = []
			results = BME280Reading.objects.filter(sensorID = criteria)
			results2 = PastBME280Readings.objects.filter(sensorID = criteria)
			for x in results:
				tempList.append(x.temperature)
				humList.append(x.humidity)
				pressList.append(x.pressure)
				labelList.append((x.timestamp).strftime("%d/%m/%Y, %H:%M:%S"))
			context = 	{	'results': results,
							'results2': results2,
							'humList': humList,
							'tempList': tempList,
							'pressList': pressList,
							'labelList': labelList,
							'idList' : idList,
							'longList': longList,
							'latList': latList,
							'sType' : sType[0],
							'lLength': lLength,
							'liveTemp': liveTemp,
							'livePress': livePress,
							'liveHumi': liveHumi,
							'historyRange':historyRange,
							'liveTimestamp':liveTimestamp,
						}
			return render(request, 'airMonitor/sensor_BME.html', context)
		elif sType[0].sensorType == "DHT22":
			tempList = []
			humList = []
			labelList = []
			results = DHT22Reading.objects.filter(sensorID = criteria )
			results2 = PastDHT22Readings.objects.filter(sensorID = criteria)
			for x in results:
				tempList.append(x.temperature)
				humList.append(x.humidity)
				labelList.append((x.timestamp).strftime("%d/%m/%Y, %H:%M:%S"))
			
			context = 	{	'results' : results,
							'results2': results2,
							'humList' : humList,
							'tempList' : tempList,
							'labelList' : labelList,
							'idList' : idList,
							'longList' : longList,
							'latList' : latList,
							'sType' : sType[0],
							'lLength' : lLength,
							'liveTemp': liveTemp,
							'liveHumi': liveHumi,
							'historyRange':historyRange,
							'liveTimestamp':liveTimestamp,
						}
			return render(request, 'airMonitor/sensor_DHT.html', context)
		else:
			results = sensorList.objects.all()
			return render(request, 'airMonitor/sensor.html', {'results': results})
	
	sensors = BME280Reading.objects.filter(humidity=90)
	return render(request, 'airMonitor/sensor.html', {'results' : sensors})

def listPage(request):
	if request.method == "POST" and 'criteria' in request.POST:
		criteria = request.POST.get('criteria', '')
		searchType = request.POST.get('searchType','')
		if criteria == '':
			sensors = sensorList.objects.all()
		elif searchType == "sensorID":
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
	longList = []
	latList  = []
	idList = []	
	longList2 = []
	latList2  = []
	idList2 = []
	sensors = sensorList.objects.all()
	SDSsensors = sensorList.objects.filter(sensorType = "SDS011")
	BMEsensors = sensorList.objects.filter(sensorType = "BME280")
	DHTsensors = sensorList.objects.filter(sensorType = "DHT22")
	if request.method == "POST":
		s1 = request.POST.get('sensor1','')
		s2 = request.POST.get('sensor2','')
		sList1 = sensorList.objects.get(sensorID=s1)
		sList2 = sensorList.objects.get(sensorID=s2)
		sType = sList1.sensorType
		idList.append(sList1.sensorID)
		longList.append(sList1.longitude)
		latList.append(sList1.latitude)
		idList2.append(sList2.sensorID)
		longList2.append(sList2.longitude)
		latList2.append(sList2.latitude)
		lLength = len(idList)

		if sType == "SDS011":
			p1List1 = []
			p2List1 = []
			p1List2 = []
			p2List2 = []
			labelList = []
			results1 = SDS011Reading.objects.filter(sensorID = s1)
			results2 = SDS011Reading.objects.filter(sensorID = s2)
			for x in results1:
				p1List1.append(x.P1)
				p2List1.append(x.P2)
				labelList.append((x.timestamp).strftime("%d/%m/%Y, %H:%M:%S"))
			for y in results2:
				p1List2.append(y.P1)
				p2List2.append(y.P2)

			context = 	{	'sensors' : sensors,
							'sType' : sType,
							'p1List1': p1List1,
							'p2List1': p2List1,
							'p1List2': p1List2,
							'p2List2': p2List2,
							'labelList': labelList,
							'sList1' : sList1,
							'sList2' : sList2,
							"SDSsensors" : SDSsensors,
							"BMEsensors" : BMEsensors,
							"DHTsensors" : DHTsensors,
							'idList' : idList,
							'longList' : longList,
							'latList' : latList,
							'idList2' : idList2,
							'longList2' : longList2,
							'latList2' : latList2,
							'lLength'	: lLength,
						}
			return render(request, 'airMonitor/comparisons.html', context)
		elif sType == "BME280":
			tempList1 = []
			humList1 = []
			pressList1 = []
			tempList2 = []
			humList2 = []
			pressList2 = []
			labelList = []
			results1 = BME280Reading.objects.filter(sensorID = s1)
			results2 = BME280Reading.objects.filter(sensorID = s2)			
			for x in results1:
				tempList1.append(x.temperature)
				humList1.append(x.humidity)
				pressList1.append(x.pressure)
				labelList.append((x.timestamp).strftime("%d/%m/%Y, %H:%M:%S"))
			for y in results2:
				tempList2.append(y.temperature)
				humList2.append(y.humidity)
				pressList2.append(y.pressure)

			context = 	{	'results1': results1,
							'sType' : sType,
							'humList1': humList1,
							'tempList1': tempList1,
							'pressList1': pressList1,
							'humList2': humList2,
							'tempList2': tempList2,
							'pressList2': pressList2,
							'labelList': labelList,
							'sList1' : sList1,
							'sList2' : sList2,
							"SDSsensors" : SDSsensors,
							"BMEsensors" : BMEsensors,
							"DHTsensors" : DHTsensors,
							'idList' : idList,
							'longList' : longList,
							'latList' : latList,
							'idList2' : idList2,
							'longList2' : longList2,
							'latList2' : latList2,
							'lLength'	: lLength,
						}
			return render(request, 'airMonitor/comparisons.html', context)
		elif sType == "DHT22":
			tempList1 = []
			humList1 = []
			tempList2 = []
			humList2 = []
			labelList = []
			results1 = DHT22Reading.objects.filter(sensorID = s1)
			results2 = DHT22Reading.objects.filter(sensorID = s2)			
			for x in results1:
				tempList1.append(x.temperature)
				humList1.append(x.humidity)
				labelList.append((x.timestamp).strftime("%d/%m/%Y, %H:%M:%S"))
			for y in results2:
				tempList2.append(y.temperature)
				humList2.append(y.humidity)
			context = 	{	'results1': results1,
							'sType' : sType,
							'humList1': humList1,
							'tempList1': tempList1,
							'humList2': humList2,
							'tempList2': tempList2,
							'labelList': labelList,
							'sList1' : sList1,
							'sList2' : sList2,
							"SDSsensors" : SDSsensors,
							"BMEsensors" : BMEsensors,
							"DHTsensors" : DHTsensors,
							'idList' : idList,
							'longList' : longList,
							'latList' : latList,
							'idList2' : idList2,
							'longList2' : longList2,
							'latList2' : latList2,
							'lLength'	: lLength,
						}
			return render(request, 'airMonitor/comparisons.html', context)
		else:
			print("ERROR!")	

		context = 	{	'sensors' : sensors,
						'sType' : sType,
						'sList1' : sList1,
						'sList2' : sList2,
						"SDSsensors" : SDSsensors,
						"BMEsensors" : BMEsensors,
						"DHTsensors" : DHTsensors,
					}
		return render(request, 'airMonitor/comparisons.html', context)	
	context = 	{	'sensors' : sensors,
					"SDSsensors" : SDSsensors,
					"BMEsensors" : BMEsensors,
					"DHTsensors" : DHTsensors,
				}
	return render(request, 'airMonitor/comparisons.html', context)	

def landing(request):
	return render(request, 'airMonitor/landing.html')