from django.shortcuts import  render, redirect
from airMonitor.models import sensorList, BME280Reading, SDS011Reading, DHT22Reading
# Create your views here.

def index(request):
	longList = []
	latList  = []
	idList = []
	results = sensorList.objects.all()
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
	if request.method == "POST":
		criteria = request.POST.get('Selection', '')
		sType = sensorList.objects.filter(sensorID = criteria) 
		if sType[0].sensorType == "SDS011":
			p1List = []
			p2List = []
			labelList = []
			results = SDS011Reading.objects.filter(sensorID = criteria)
			for x in results:
				p1List.append(x.P1)
				p2List.append(x.P2)
				labelList.append((x.timestamp).strftime("%d/%m/%Y, %H:%M:%S"))
			context = 	{	'results': results,
							'p1List': p1List,
							'p2List': p2List,
							'labelList': labelList
						}
			return render(request, 'airMonitor/sensor_SDS.html', context)
		elif sType[0].sensorType == "BME280":
			tempList = []
			humList = []
			pressList = []
			labelList = []
			results = BME280Reading.objects.filter(sensorID = criteria)
			for x in results:
				tempList.append(x.temperature)
				humList.append(x.humidity)
				pressList.append(x.pressure)
				labelList.append((x.timestamp).strftime("%d/%m/%Y, %H:%M:%S"))
			context = 	{	'results': results,
							'humList': humList,
							'tempList': tempList,
							'pressList': pressList,
							'labelList': labelList
						}
			return render(request, 'airMonitor/sensor_BME.html', context)
		elif sType[0].sensorType == "DHT22":
			tempList = []
			humList = []
			labelList = []
			results = DHT22Reading.objects.filter(sensorID = criteria)
			for x in results:
				tempList.append(x.temperature)
				humList.append(x.humidity)
				labelList.append((x.timestamp).strftime("%d/%m/%Y, %H:%M:%S"))
			context = 	{	'results': results,
							'humList': humList,
							'tempList': tempList,
							'labelList': labelList
						}
			return render(request, 'airMonitor/sensor_DHT.html', context)
		else:
			return render(request, 'airMonitor/sensor.html', {'results': results})

	return render(request, 'airMonitor/sensor.html')

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