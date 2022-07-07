import csv
import os
import requests
import urllib, json
from pathlib import Path
from django.db import models
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from airMonitor.models import sensorList, BME280Reading, SDS011Reading, DHT22Reading

class Command(BaseCommand):
	help = 'Load data from json'
	def handle(self, *args, **options):
		#sensorList.objects.all().delete()
		#BME280Reading.objects.all().delete()
		#SDS011Reading.objects.all().delete()
		#DHT22Reading.objects.all().delete()

		json_url = requests.get("https://raw.githubusercontent.com/scharlau/Air_Aberdeen_Back_End/main/data/bq_data.json")
		data = json_url.json()
		#print(data)

		listOfSensorID=[]
		for x in data:
			listOfSensorID.append(""+x["sensor_id"]+","+x["sensor_type"]+","+x["latitude"]+","+x["longitude"]+","+x["location_id"])
		listOfSensorID = list(set(listOfSensorID))

		for newSensor in listOfSensorID:
			arr = newSensor.split(',')
			try:
				sList = sensorList.objects.create(
					sensorID = arr[0],
					sensorType = arr[1],
					latitude  = arr[2],
					longitude = arr[3],
					location_id = arr[4],
					)
				sList.save()
				print("Completed Row:",arr[0])
			except:
  				print(arr[0],"This sensor exists")


		listOfBME280Readings =[]
		listOfSDS011Readings =[]
		listOfDHT22Readings =[]

		for y in data:
			if y["sensor_type"] == "BME280":
				shortDate = y["timestamp"]+"-01:00"
				listOfBME280Readings.append(""+y["sensor_id"]+","+shortDate+","+y["humidity"]+","+y["pressure"]+","+y["temperature"])
			elif y["sensor_type"] == "SDS011":
				shortDate = y["timestamp"]+"-01:00"
				listOfSDS011Readings.append(""+y["sensor_id"]+","+shortDate+","+y["P1"]+","+y["P2"])
			elif y["sensor_type"] == "DHT22":
				shortDate = y["timestamp"]+"-01:00"
				listOfDHT22Readings.append(""+y["sensor_id"]+","+shortDate+","+y["humidity"]+","+y["temperature"])
			else:
				print("Invalid Sensor Type")
			#print(y)

		for a in listOfBME280Readings:
			arr = a.split(',')
			sList = BME280Reading.objects.create(
				sensorID = sensorList.objects.get(sensorID=arr[0]),
				timestamp = arr[1],
				humidity  = arr[2],
				pressure = arr[3],
				temperature = arr[4],
				)
			print("Completed BME280 Reading:",arr[0],arr[1])
		print("Completed BME280 Readings")

		for b in listOfSDS011Readings:
			arr = b.split(',')
			sList = SDS011Reading.objects.create(
				sensorID = sensorList.objects.get(sensorID=arr[0]),
				timestamp = arr[1],
				P1  = arr[2],
				P2 = arr[3],
				)
			print("Completed SDS011 Reading:",arr[0],arr[1])
		print("Completed SDS011 Readings")

		for c in listOfDHT22Readings:
			arr = c.split(',')
			sList = DHT22Reading.objects.create(
				sensorID = sensorList.objects.get(sensorID=arr[0]),
				timestamp = arr[1],
				humidity  = arr[2],
				temperature = arr[3],
				)
			print("Completed DHT22 Reading:",arr[0],arr[1])
		print("Completed DHT22 Readings")
