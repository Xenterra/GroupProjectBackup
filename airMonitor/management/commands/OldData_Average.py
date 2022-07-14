import csv
import os
import requests
import urllib, json
import math
from pathlib import Path
from django.db import models
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from airMonitor.models import sensorList, BME280Reading, SDS011Reading, DHT22Reading, PastBME280Readings, PastDHT22Readings, PastSDS011Readings
from datetime import datetime, timedelta, time


class Command(BaseCommand):
	help = 'Load data from json'
	def handle(self, *args, **options):
		#PastBME280Readings.objects.all().delete()
		#PastDHT22Readings.objects.all().delete()
		#PastSDS011Readings.objects.all().delete()

		listOfSensorID=[]
		listOfSensorID = sensorList.objects.all()
		time1 = datetime.now() - timedelta(days=8)
		now=datetime.combine(time1, datetime.min.time())


		for sensor in listOfSensorID:
			listOfOldSDS = []
			listOfOldBME = []
			listOfOldDHT = []
			if sensor.sensorType == "SDS011":
				a=SDS011Reading.objects.filter(sensorID=sensor,timestamp__lt=now)
				for reading in a:
					listOfOldSDS.append((reading.P1,reading.P2))
			elif sensor.sensorType == "BME280":
				b=BME280Reading.objects.filter(sensorID=sensor,timestamp__lt=now)
				for reading in b:
					listOfOldBME.append((reading.temperature,reading.humidity,reading.pressure))
			elif sensor.sensorType == "DHT22":
				c=DHT22Reading.objects.filter(sensorID=sensor,timestamp__lt=now)
				for reading in c:
					listOfOldDHT.append((reading.temperature,reading.humidity))
			else:
				print("Unregistered sensor discovered")


			targetTime = now - timedelta(days=1)
			if len(listOfOldSDS) != 0:
				totalP1 = 0
				totalP2 = 0
				averageP1 = 0
				averageP2 = 0
				for x in listOfOldSDS:
					totalP1 += x[0]
					totalP2 += x[1]
				averageP1 = round(totalP1/len(listOfOldSDS),2)
				averageP2 = round(totalP2/len(listOfOldSDS),2)
				PastSDS011Readings.objects.create(
					sensorID = sensorList.objects.get(sensorID=sensor.sensorID),
					pastDate = targetTime,
					dailyAverageP1 = averageP1,
					dailyAverageP2= averageP2,
					)
			elif len(listOfOldBME) != 0:
				totalTemperature = 0
				totalHumidity = 0
				totalPressure = 0
				averageTemperature = 0
				averageHumidity = 0
				averagePressure = 0
				for x in listOfOldBME:
					totalTemperature += x[0]
					totalHumidity += x[1]
					totalPressure += x[2]
				averageTemperature = round(totalTemperature/len(listOfOldBME),2)
				averageHumidity = round(totalHumidity/len(listOfOldBME),2)
				averagePressure = round(totalPressure/len(listOfOldBME),2)
				PastBME280Readings.objects.create(
					sensorID = sensorList.objects.get(sensorID=sensor.sensorID),
					pastDate = targetTime,
					dailyAverageHumidity = averageHumidity,
					dailyAverageTemperature = averageTemperature,
					dailyAveragePressure = averagePressure,
					)			
			elif len(listOfOldDHT) != 0:
				totalTemperature = 0
				totalHumidity = 0
				averageTemperature = 0
				averageHumidity = 0
				for x in listOfOldDHT:
					totalTemperature += x[0]
					totalHumidity += x[1]
				averageTemperature = round(totalTemperature/len(listOfOldDHT),2)
				averageHumidity = round(totalHumidity/len(listOfOldDHT),2)
				PastDHT22Readings.objects.create(
					sensorID = sensorList.objects.get(sensorID=sensor.sensorID),
					pastDate = targetTime,
					dailyAverageHumidity = averageHumidity,
					dailyAverageTemperature = averageTemperature,
				)
			print(sensor.sensorType, "Previous Day Average Collected")


		SDS011Reading.objects.filter(timestamp__lt=now).delete()
		BME280Reading.objects.filter(timestamp__lt=now).delete()
		DHT22Reading.objects.filter(timestamp__lt=now).delete()
		print("Old Data has been cleared")
