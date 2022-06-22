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
		verbose_name = "SensorList"
		verbose_name_plural = "SensorLists"

class BME280Reading(models.Model):
	uniqueID = models.IntegerField(primary_key=True)
	sensorID = models.ForeignKey("sensorList", on_delete=models.CASCADE)
	timestamp = models.DateTimeField()
	humidity = models.FloatField()
	temperature = models.FloatField()
	pressure = models.FloatField()

	class Meta:
		db_table = "BME280Reading"
		verbose_name = "BME280"
		verbose_name_plural = "BME280s"

class DHT22Reading(models.Model):
	uniqueID = models.IntegerField(primary_key=True)
	sensorID = models.ForeignKey("sensorList", on_delete=models.CASCADE)
	timestamp = models.DateTimeField()
	humidity = models.FloatField()
	temperature = models.FloatField()

	class Meta:
		db_table = "DHT22Reading"
		verbose_name = "DHT22"
		verbose_name_plural = "DHT22s"

class SDS011Reading(models.Model):
	uniqueID = models.IntegerField(primary_key=True)
	sensorID = models.ForeignKey("sensorList", on_delete=models.CASCADE)
	timestamp = models.DateTimeField()
	P1 = models.FloatField()
	P2 = models.FloatField()

	class Meta:
		db_table = "SDS011Reading"
		verbose_name = "SDS011"
		verbose_name_plural = "SDS011s"