from django.conf.urls.defaults import url, patterns
from django.views.generic.simple import direct_to_template
from views import *

urlpatterns = patterns('',
	url(r'^$', to_english),
	url(r'^(?P<lang_code>[a-z]{2})/$', index),
	url(r'^(?P<lang_code>[a-z]{2})/landlords/$', landlords),
	url(r'^(?P<lang_code>[a-z]{2})/tenants/$', tenants),
	url(r'^(?P<lang_code>[a-z]{2})/buyers/$', buyers),
	url(r'^sellers/$', direct_to_template, {'template': 'pages/sellers.html'}),
	url(r'^(?P<lang_code>[a-z]{2})/corporate/$', corporate),
	url(r'^(?P<lang_code>[a-z]{2})/about_us/(?P<subpage>[a-z_]+)/$', about_us),
	url(r'^(?P<lang_code>[a-z]{2})/search/$', search),
	url(r'^(?P<lang_code>[a-z]{2})/landlord_services/(?P<service_name>[a-z_]+)/$', landlord_services),
	url(r'^(?P<lang_code>[a-z]{2})/city_guide/(?P<area>[a-z_]+)/$', city_guide, name = 'city_guide'),
	url(r'^(?P<lang_code>[a-z]{2})/currency_exchange/$', currency_exchange),
	url(r'^(?P<lang_code>[a-z]{2})/faq/$', faq),
	url(r'^(?P<lang_code>[a-z]{2})/detail/(?P<prop_id>[0-9]+)/$', detail),
	url(r'^our_properties/$', direct_to_template, {'template': 'pages/our_properties.html'}, name = 'our_properties'),
	#url(r'^map_test/$', map_test), # Just for testing map related functions
)