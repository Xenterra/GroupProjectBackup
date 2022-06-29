import csv
import os
import json
from pathlib import Path
from django.db import models
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from airMonitor.models import sensorList, BME280Reading, SDS011Reading, DHT22Reading

class Command(BaseCommand):
	help = 'Load data from json'
	def handle(self, *args, **options):
		sensorList.objects.all().delete()
		BME280Reading.objects.all().delete()
		SDS011Reading.objects.all().delete()
		DHT22Reading.objects.all().delete()

		fileObject = open("bq_data.json", "r")
		jsonContent = fileObject.read()
		aList = json.loads(jsonContent)
		listOfSensorID =[]

		for x in aList:
			listOfSensorID.append(""+x["sensor_id"]+","+x["sensor_type"]+","+x["latitude"]+","+x["longitude"]+","+x["location_id"])
		listOfSensorID = list(set(listOfSensorID))
		for y in listOfSensorID:
			arr = y.split(',')
			sList = sensorList.objects.create(
				sensorID = arr[0],
				sensorType = arr[1],
				latitude  = arr[2],
				longitude = arr[3],
				location_id = arr[4],
				)
			sList.save()
			print("Completed Row:",arr[0])

		listOfBME280Readings =[]
		listOfSDS011Readings =[]
		listOfDHT22Readings =[]

		for x in aList:
			if x["sensor_type"] == "BME280":
				shortDate = x["timestamp"]+"-01:00"
				listOfBME280Readings.append(""+x["sensor_id"]+","+shortDate+","+x["humidity"]+","+x["pressure"]+","+x["temperature"])
			elif x["sensor_type"] == "SDS011":
				shortDate = x["timestamp"]+"-01:00"
				listOfSDS011Readings.append(""+x["sensor_id"]+","+shortDate+","+x["P1"]+","+x["P2"])
			elif x["sensor_type"] == "DHT22":
				shortDate = x["timestamp"]+"-01:00"
				listOfDHT22Readings.append(""+x["sensor_id"]+","+shortDate+","+x["humidity"]+","+x["temperature"])
			else:
				print("Invalid Sensor Type")

		for a in listOfBME280Readings:
			arr = a.split(',')
			sList = BME280Reading.objects.create(
				sensorID = sensorList.objects.get(sensorID=arr[0]),
				timestamp = arr[1],
				humidity  = arr[2],
				pressure = arr[3],
				temperature = arr[4],
				)
			#print("Completed BME280 Reading:",arr[0],arr[1])
		print("Completed BME280 Readings")

		for b in listOfSDS011Readings:
			arr = b.split(',')
			sList = SDS011Reading.objects.create(
				sensorID = sensorList.objects.get(sensorID=arr[0]),
				timestamp = arr[1],
				P1  = arr[2],
				P2 = arr[3],
				)
			#print("Completed SDS011 Reading:",arr[0],arr[1])
		print("Completed SDS011 Readings")

		for c in listOfDHT22Readings:
			arr = c.split(',')
			sList = DHT22Reading.objects.create(
				sensorID = sensorList.objects.get(sensorID=arr[0]),
				timestamp = arr[1],
				humidity  = arr[2],
				temperature = arr[3],
				)
			#print("Completed DHT22 Reading:",arr[0],arr[1])
		print("Completed DHT22 Readings")
