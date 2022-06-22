from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.sensorList)
admin.site.register(models.BME280Reading)
admin.site.register(models.SDS011Reading)
admin.site.register(models.DHT22Reading)