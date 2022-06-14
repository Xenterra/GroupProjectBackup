from django.db import models

# Create your models here.
class sensorList(models.Model):
	sensorID = models.IntegerField(primary_key=True)
	longitude = models.FloatField()
	latitude = models.FloatField()
	sensorType = models.CharField(max_length=200)
	location_id = models.IntegerField()

	class Meta:
		db_table = "sensorList"

class BME280Reading(models.Model):
	uniqueID = models.IntegerField(primary_key=True)
	sensorID = models.ForeignKey("sensorList", on_delete=models.CASCADE)
	timestamp = models.DateTimeField()
	humidity = models.FloatField()
	temperature = models.FloatField()
	pressure = models.FloatField()

	class Meta:
		db_table = "BME280Reading"

class DHT22Reading(models.Model):
	uniqueID = models.IntegerField(primary_key=True)
	sensorID = models.ForeignKey("sensorList", on_delete=models.CASCADE)
	timestamp = models.DateTimeField()
	humidity = models.FloatField()
	temperature = models.FloatField()

	class Meta:
		db_table = "DHT22Reading"

class SDS011Reading(models.Model):
	uniqueID = models.IntegerField(primary_key=True)
	sensorID = models.ForeignKey("sensorList", on_delete=models.CASCADE)
	timestamp = models.DateTimeField()
	P1 = models.FloatField()
	P2 = models.FloatField()

	class Meta:
		db_table = "SDS011Reading"