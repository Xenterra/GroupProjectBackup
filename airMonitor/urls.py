from django.urls import path
from . import views

urlpatterns = [
	path('', views.landing, name='landing'),
	path('map/', views.index, name='index'),
	path('sensor/', views.sensor, name='sensor'),
	path('sensorListPage/', views.listPage, name='listPage'),
	path('comparisons/', views.comparisons, name='comparisons'),

]