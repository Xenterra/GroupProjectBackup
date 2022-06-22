import urllib
from urllib.parse import urljoin, urlparse
from behave import given, when, then, model
from django.conf import settings
from django.shortcuts import resolve_url
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'we want to view the list of sensors')
def user_on_index_page(context):
	#print("Cart Given Step Here:")
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
