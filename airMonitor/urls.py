from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('sensor/', views.sensor, name='sensor'),
	path('sensorListPage/', views.sensorListPage, name='sensorListPage'),
	path('comparisons/', views.comparisons, name='comparisons'),

]