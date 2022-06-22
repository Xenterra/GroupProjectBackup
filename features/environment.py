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

CHROME_DRIVER = os.path.join("driver/chromedriver")
chrome_options = Options()

#chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-proxy-server")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")


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
	context.test_case = LiveServerTestCase
	context.test_case.setUpClass()
	yield
	context.test_case.tearDownClass()
	del context.test_case
