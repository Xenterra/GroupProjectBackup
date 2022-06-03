from django.db import models

# Create your models here.
class sensorList(models.Model):
	sensorID = models.IntegerField(primary_key=True)
	longitude = models.FloatField()
	latitude = models.FloatField()
	installDate = models.DateField()

	class Meta:
		db_table = "sensorList"

class sensor1(models.Model):
	timestamp = models.IntegerField(primary_key=True)
	P1 = models.FloatField()
	P2 = models.FloatField()
	humidity = models.FloatField()
	temperature = models.FloatField()

	class Meta:
		db_table = "sensor1"