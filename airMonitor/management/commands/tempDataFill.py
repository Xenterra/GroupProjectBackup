import csv
import os
from pathlib import Path
from django.db import models
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from airMonitor.models import sensorList, sensor1

class Command(BaseCommand):
	help = 'Load data from csv'
	def handle(self, *args, **options):
		sensorList.objects.all().delete()
		sensor1.objects.all().delete()
		# Refill the model database
		with open('sensorDetails_Prototype.csv', newline='') as f:
			reader = csv.reader(f, delimiter=",")
			next(reader) # skip the header line
			for row in reader:
				if row[0] != '':
					sList = sensorList.objects.create(
					sensorID = row[0],
					longitude = row[1],
					latitude  = row[2],
					installDate = row[3],
					)
					sList.save()
				print("Completed Row:",row[0])
			print("Sensor Install Complete")

		with open('sensor1.csv', newline='') as f:
			reader = csv.reader(f, delimiter=",")
			next(reader) # skip the header line
			for row in reader:
				if row[0] != '':
					s1List = sensor1.objects.create(
					timestamp = row[0],
					P1 = row[1],
					P2 = row[2],
					humidity = row[3],
					temperature = row[4],
					)
					s1List.save()
				print("Completed Row:",row[0])
			print("Sensor1 Details List Complete")