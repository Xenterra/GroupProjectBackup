import urllib
from urllib.parse import urljoin, urlparse
from behave import given, when, then, model
from django.conf import settings
from django.shortcuts import resolve_url


@given(u'we want to compare different sensors of the same type')
def user_on_index_page(context):
	#print("Cart Given Step Here:")
	base_url = urllib.request.url2pathname(context.test_case.live_server_url)
	#print(base_url)
	open_url = urljoin(base_url,'/')
	context.browser.get(open_url)

@when(u'we click on the comparison link')
def user_clicks_comparison_button(context):
	context.browser.find_element_by_name('comparisonLink').click()

@then(u'the comparison page opens')
def Comparison_page_opens(context):
	assert 'comparisonPage' in context.browser.page_source
