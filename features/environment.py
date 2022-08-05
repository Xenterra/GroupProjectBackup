# -- FILE: features/environment.py
from behave import *
from behave import fixture, use_fixture
import os, urllib
import django

os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"
django.setup()

from django.test import selenium, TransactionTestCase, RequestFactory
from django.test.testcases import TestCase
from django.contrib.auth.models import User
from django.test.runner import DiscoverRunner
from django.test.testcases import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from airMonitor.models import sensorList, BME280Reading

CHROME_DRIVER = os.path.join("driver/chromedriver")
chrome_options = Options()

#chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-proxy-server")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")

class BaseTestCase(LiveServerTestCase):
	@classmethod
	def setUpClass(cls):
		sensorList.objects.create(sensorID="134256724", longitude="57.1499", latitude="-2.0938", sensorType="BME280", location_id = "1234").save()
		BME280Reading.objects.create(uniqueID=1, sensorID=sensorList.objects.get(sensorID=134256724),  timestamp="2021-01-01T00:00:01", humidity=100.0, temperature = 13.87, pressure= 100401.97).save()
		super(BaseTestCase, cls).setUpClass()
 	 	 
	@classmethod
	def tearDownClass(cls):
		sensorList.objects.filter().delete()
		BME280Reading.objects.filter().delete()
		super(BaseTestCase, cls).tearDownClass()


def before_all(context):
	use_fixture(django_test_runner, context)
	context.browser = webdriver.Chrome(options=chrome_options, executable_path=CHROME_DRIVER)
	context.browser.set_page_load_timeout(time_to_wait=200)

def before_scenario(context, scenario):
	context.test = TransactionTestCase() 
	context.test.setUpClass()
	use_fixture(django_test_case, context)

def after_scenario(context, scenario):
	context.test.tearDownClass()
	del context.test

def after_all(context):
	context.browser.quit()	

def django_test_runner(context):
	context.test_runner = DiscoverRunner()
	context.test_runner.setup_test_environment()
	context.old_db_config = context.test_runner.setup_databases()
	yield
	context.test_runner.teardown_databases(context.old_db_config)
	context.test_runner.teardown_test_environment()

@fixture
def django_test_case(context):
	context.test_case = BaseTestCase
	context.test_case.setUpClass()
	yield
	context.test_case.tearDownClass()
	del context.test_case
