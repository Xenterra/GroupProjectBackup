from django.urls import path
from . import views

urlpatterns = [
	path('', views.landing, name='landing'),
	path('map/', views.index, name='index'),
	path('sensor/', views.sensor, name='sensor'),
	path('sensorListPage/', views.listPage, name='listPage'),
	path('comparisons/', views.comparisons, name='comparisons'),
	path('User_guide/', views.User_guide, name='User_guide'),
	path('FAQs/', views.FAQs, name='FAQs'),

    #path('download/', views3.download_file),
    #path('downloadpdf/', views2.download_pdf_file, name='download_pdf_file'),
    #path('downloadpdf//', views2.download_pdf_file, name='download_pdf_file'),

]