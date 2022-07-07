import csv
import os
import requests
import urllib, json
import math
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

		for y in data:
			newTemperature = 0.0
			newHumidity = 0.0
			newPressure = 0.0
			newP1 = 0.0
			newP2 = 0.0
			if y["sensor_type"] == "BME280":
				shortDate = y["timestamp"]+"-00:00"
				try:
					if math.isnan(y["humidity"]):
						newHumidity = 100.0
					else:
						newHumidity = 0.0+float(y["humidity"])
				except:
					newHumidity = "100.0"
				try:
					if math.isnan(y["pressure"]):
						newPressure = 0.0
					else:
						newPressure = 0.0+float(y["pressure"])
				except:
					newPressure = "0.0"
				try:
					if math.isnan(y["temperature"]):
						newTemperature = 0.0
					else:
						newTemperature = 0.0+float(y["temperature"])
				except:
					newTemperature = "0.0"

				sList = BME280Reading.objects.create(
						sensorID = sensorList.objects.get(sensorID=y["sensor_id"]),
						timestamp = shortDate,
						humidity  = newHumidity,
						pressure = newPressure,
						temperature = newTemperature,
						)
				print("Completed BME280 Reading:",y["sensor_id"],shortDate)

			elif y["sensor_type"] == "SDS011":
				shortDate = y["timestamp"]+"-00:00"				
				try:
					if math.isnan(y["P1"]):
						newP1 = 0.0
					else:
						newP1 = 0.0+float(y["P1"])
				except:
					newP1 = "0.0"
				try:
					if math.isnan(y["P2"]):
						newP2 = 0.0
					else:
						newP2 = 0.0+float(y["P2"])
				except:
					newP2 = "0.0"

				sList = SDS011Reading.objects.create(
						sensorID = sensorList.objects.get(sensorID=y["sensor_id"]),
						timestamp = shortDate,
						P1  = newP1,
						P2 = newP2,
						)
				print("Completed SDS011 Reading:",y["sensor_id"],shortDate)
			elif y["sensor_type"] == "DHT22":
				shortDate = y["timestamp"]+"-00:00"
				try:
					if math.isnan(y["humidity"]):
						newHumidity = 100.0
					else:
						newHumidity = 0.0+float(y["humidity"])
				except:
					newHumidity = "100.0"
				try:
					if math.isnan(y["temperature"]):
						newTemperature = 0.0
					else:
						newTemperature = 0.0+float(y["temperature"])
				except:
					newTemperature = "0.0"

				sList = DHT22Reading.objects.create(
						sensorID = sensorList.objects.get(sensorID=y["sensor_id"]),
						timestamp = shortDate,
						humidity  = newHumidity,
						temperature = newTemperature,
						)
				print("Completed DHT22 Reading:",y["sensor_id"],shortDate)
			else:
				print("Invalid Sensor Type")