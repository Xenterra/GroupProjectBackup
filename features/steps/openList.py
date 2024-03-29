import urllib
from urllib.parse import urljoin, urlparse
from behave import given, when, then, model
from django.conf import settings
from django.shortcuts import resolve_url
from selenium.webdriver.common.by import By

# Scenario 1: Get a list of all sensors in the system
@given(u'we want to view the list of sensors')
def user_on_index_page(context):
	base_url = urllib.request.url2pathname(context.test_case.live_server_url)
	#print(base_url)
	open_url = urljoin(base_url,'/')
	context.browser.get(open_url)

@when(u'we click the List link')
def user_clicks_list_button(context):
	context.browser.find_element_by_name('listLink').click()

@then(u'the page opens')
def list_page_opens(context):
	assert 'listPage' in context.browser.page_source 


# Scenario 2: Get details of one sensor
@given(u'I want to find out more details of one sensor in the system')
def user_on_index_page(context):
	base_url = urllib.request.url2pathname(context.test_case.live_server_url)
	open_url = urljoin(base_url,'/')
	context.browser.get(open_url)

@when(u'I click the List link')
def user_clicks_list_button(context):
	context.browser.find_element_by_name('listLink').click()

@then(u'I click the More Details button')
def step_impl(context):
	context.browser.find_element_by_name('Selection').click()

@then(u'I go to the Sensor Details page (the Sensor Details page opens)')
def list_page_opens(context):
	assert 'BMEdetailsPage' in context.browser.page_source