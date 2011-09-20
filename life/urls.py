from django.conf.urls.defaults import url, patterns
from django.views.generic.simple import direct_to_template
from views import *

urlpatterns = patterns('',
	url(r'^$', to_english),
	url(r'^(?P<lang_code>[a-z]{2})/$', index),
	url(r'^(?P<lang_code>[a-z]{2})/landlords/$', landlords),
	url(r'^tenants/$', direct_to_template, {'template': 'pages/tenants.html'}, name = 'tenants'),
	url(r'^buyers/$', direct_to_template, {'template': 'pages/buyers.html'}, name = 'buyers'),
	url(r'^sellers/$', direct_to_template, {'template': 'pages/sellers.html'}, name = 'sellers'),
	url(r'^corporate/$', direct_to_template, {'template': 'pages/corporate.html'}, name = 'corporate'),
	url(r'^about_us/(?P<subpage>[a-z_]+)/$', about_us, name = 'about_us'),
	url(r'^search/$', search, name = 'search'),
	url(r'^landlord_services/(?P<service_name>[a-z_]+)/$', landlord_services, name = 'landlord_services'),
	url(r'^city_guide/(?P<area>[a-z_]+)/$', city_guide, name = 'city_guide'),
	url(r'^currency_exchange/$', direct_to_template, {'template': 'pages/currency_exchange.html'}, name = 'currency_exchange'),
	url(r'^faq/$', direct_to_template, {'template': 'pages/faq.html'}, name = 'faq'),
	url(r'^detail/$', direct_to_template, {'template': 'pages/detail.html'}, name = 'detail'),
	url(r'^our_properties/$', direct_to_template, {'template': 'pages/our_properties.html'}, name = 'our_properties'),
)