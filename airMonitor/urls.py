from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('sensor/', views.sensor, name='sensor'),
	path('sensorList/', views.sensorList, name='sensorList'),
	path('comparisons/', views.comparisons, name='comparisons'),

]