from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from models import *
from random import shuffle
from json import loads as parse_json
from re import sub, match

def generate_base_dict(lang_code, pagename):
	languages = [(langobj.lang_code, langobj.lang) for langobj in Language.objects.all()]
	
	for language in languages: # The current langauge need to be selected
		if language[0] == lang_code:
			languages.remove(language)
			languages = [language] + languages
			break
	
	return {'pagename': pagename, 'curr_lang_code': lang_code, 'curr_lang': Language.objects.filter(lang_code = lang_code)[0].lang, 'curr_flag': Language.objects.filter(lang_code = lang_code)[0].flag, 'languages': languages}
	

def add_searchform(template_dict):
	# TODO: should change after adding translations and shit...
	template_dict['searchform_types'] = type_choices
	
	template_dict['sales_min_prices'] = [25000 * i for i in range(1,17)] + [450000] + [i * 100000 for i in range(5,10)]
	template_dict['sales_max_prices'] = [25000 * i for i in range(2,17)] + [450000] + [i * 100000 for i in range(5,10)] + [1000000]
	template_dict['rentals_min_prices'] = [250 * i for i in range(1,9)] + [500 * i for i in range(5,10)]
	template_dict['rentals_max_prices'] = [250 * i for i in range(2,9)] + [500 * i for i in range(5,10)] + [5000]
	
	template_dict['min_bedrooms'] = [i for i in range(7)]
	template_dict['max_bedrooms'] = [i for i in range(1,8)]
	
	return template_dict
	
def add_testimonials(template_dict):
	template_dict['testimonials'] = [(t.testimonial.name, t.testimonial.date, t.quote) for t in TestimonialTranslation.objects.filter(language__lang_code = template_dict['curr_lang_code'])]
	
	return template_dict
	
def add_staff(template_dict):
	template_dict['staff'] = StaffMember.objects.all()

	return template_dict
	
def landlord_services(request, service_name, lang_code):
	if service_name not in ['property_management', 'tax_advice', 'furnishing', 'client_info', 'engagement_terms']:
		service_name = 'landlord_services' # put base in list and redirect to base if not in list...
		
	template_dict = generate_base_dict(lang_code, '/city_guide/' + service_name + '/')
	
	template_dict['service_name'] = service_name
		
	if service_name == 'property_management':
		template_dict['selflink_text'] = 'Property Management'
	elif service_name == 'tax_advice':
		template_dict['selflink_text'] = 'Tax Advice'
	elif service_name == 'furnishing':
		template_dict['selflink_text'] = 'Furnitures Sales/Rental'
	elif service_name == 'client_info':
		template_dict['selflink_text'] = 'Client Information'
	elif service_name == 'engagement_terms':
		template_dict['selflink_text'] = 'Terms of Engagement'
	else:
		template_dict['selflink_text'] = ''
		
	template_dict['content_name'] = 'elements/landlord_services_content/' + service_name + '.html'
		
	return render_to_response('pages/landlord_services.html', template_dict, context_instance = RequestContext(request))
	
def city_guide(request, area, lang_code):
	if area not in ['central']:
		area = 'all'
	
	template_dict = generate_base_dict(lang_code, '/city_guide/' + area + '/')
	
	template_dict['area_name'] = area
		
	template_dict['content_name'] = 'elements/city_guide_content/' + area + '.html'
	
	if area == 'all':
		template_dict['container_class'] = 'page guide'
	else:
		template_dict['container_class'] = 'page guide area'
		
	template_dict = add_staff(template_dict)
	template_dict = add_testimonials(template_dict)
		
	return render_to_response('pages/city_guide.html', template_dict, context_instance = RequestContext(request))

def about_us(request, subpage, lang_code):
	if subpage not in ['recruitment', 'our_staff']:
		subpage = 'base'
		
	template_dict = generate_base_dict(lang_code, '/about_us/' + subpage + '/')
	
	template_dict['subpage'] = subpage
	
	template_dict['content_name'] = 'elements/about_us_content/' + subpage + '.html'

	if subpage in ['base', 'recruitment']:
		template_dict['real_content_id'] = 'about'
	else:
		template_dict['real_content_id'] = 'staff'
		
	if subpage == 'base':
		template_dict['container_class'] = 'page about'
	elif subpage == 'recruitment':
		template_dict['container_class'] = 'page about recruitment'
	else:
		template_dict['container_class'] = 'page staff'
	
	if subpage != 'our_staff':
		template_dict['slider_images'] = ['images/about_image.jpg', 'images/about_image_2.jpg', 'images/about_image.jpg', 'images/about_image_2.jpg']
		
	template_dict = add_staff(template_dict)
	template_dict = add_testimonials(template_dict)
	if subpage == 'our_staff':
		template_dict['offices'] = [OfficeDummy(range(1,3)) for i in range(2)]
	
	return render_to_response('pages/about_us.html', template_dict, context_instance = RequestContext(request))
	
def index(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/')
	
	template_dict = add_searchform(template_dict)
	template_dict = add_staff(template_dict)
	template_dict = add_testimonials(template_dict)
	
	return render_to_response('pages/index.html', template_dict, context_instance = RequestContext(request))
	
def to_english(request):
	return redirect('/uk/')
	
def search(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/search/')
	if request.method == 'POST':
		query_dict = {}

		if 'shortlist_ids' in request.POST:
			print 'shortlist_ids', request.POST['shortlist_ids']
			query_dict['property_id__in'] = parse_json(request.POST['shortlist_ids'])
		else:
			query_dict['sale_type'] = request.POST['sale_type']
			
			placeholder = TextElementTranslation.objects.filter(language__lang_code = lang_code, element_name__element_name = 'searchboxes-form-location_placeholder')[0].element_text
			if request.POST['district'] != placeholder:
				query_dict['district__name__icontains'] = request.POST['district']
			
			if request.POST['type'] != 'NA':
				query_dict['type'] = request.POST['type']
			
			query_dict['price__gte'] = request.POST['min_price']
			query_dict['price__lte'] = request.POST['max_price']
			query_dict['bed_count__gte'] = request.POST['min_bedrooms']
			query_dict['bed_count__lte'] = request.POST['max_bedrooms']

		print query_dict

		template_dict['search_results'] = Property.objects.filter(**query_dict).order_by('price')
	else:
		template_dict['search_results'] = Property.objects.all().order_by('price')

	template_dict['property_ids'] = [p.property_id for p in template_dict['search_results']]

	# Gathering images for the properties
	for i in range(len(template_dict['search_results'])):
		template_dict['search_results'][i].searchimages = [sub(r'(.*/)([^/]+)', r'\1searchpage/\2', j.image.name) for j in PropertyThumbnail.objects.filter(property__property_id = template_dict['search_results'][i].property_id)][1:5]

	for result in template_dict['search_results']:
		desc = PropertyDescription.objects.filter(language__lang_code = lang_code, property__property_id = result.property_id)[0].description
		if len(desc) >= 150:
			result.description = desc[:150] + '...'
		else:
			result.description = desc
	
	template_dict = add_searchform(template_dict)
	template_dict = add_testimonials(template_dict)

	price_low_to_high_text = TextElementTranslation.objects.filter(language__lang_code = lang_code, element_name__element_name = 'search-ordering_price_low_to_high')[0].element_text
	price_high_to_low_text = TextElementTranslation.objects.filter(language__lang_code = lang_code, element_name__element_name = 'search-ordering_price_high_to_low')[0].element_text
	template_dict['ordering_dict'] = {'plh': price_low_to_high_text, 'phl': price_high_to_low_text};
	template_dict['default_ordering'] = 'plh'

	all_text = TextElementTranslation.objects.filter(language__lang_code = lang_code, element_name__element_name = 'search-all_text')[0].element_text
	template_dict['result_per_page_dict'] = [(5,'5'), (10,'10'), (15,'15'), (99999999, all_text)]
	template_dict['default_result_per_page'] = 5
	
	return render_to_response('pages/search.html', template_dict, context_instance = RequestContext(request))
	
def landlords(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/landlords/')
	
	template_dict['previous_developments'] = [TestimonialDummy('/images/prev_dev_thumb1.jpg', 'Cadwell House, London SW13') for i in range(3)]
	template_dict = add_testimonials(template_dict)
	
	return render_to_response('pages/landlords.html', template_dict, context_instance = RequestContext(request))
	
def tenants(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/tenants/')
	
	template_dict = add_searchform(template_dict)
	template_dict = add_staff(template_dict)
	template_dict = add_testimonials(template_dict)
	
	return render_to_response('pages/tenants.html', template_dict, context_instance = RequestContext(request))

def buyers(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/buyers/')

	template_dict = add_searchform(template_dict)
	template_dict = add_staff(template_dict)
	template_dict = add_testimonials(template_dict)

	return render_to_response('pages/buyers.html', template_dict, context_instance = RequestContext(request))

def corporate(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/corporate/')

	template_dict = add_searchform(template_dict)
	template_dict = add_staff(template_dict)
	template_dict = add_testimonials(template_dict)

	return render_to_response('pages/corporate.html', template_dict, context_instance = RequestContext(request))
	
def currency_exchange(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/currency_exchange/')

	template_dict = add_searchform(template_dict)
	template_dict = add_testimonials(template_dict)

	return render_to_response('pages/corporate.html', template_dict, context_instance = RequestContext(request))
	
def faq(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/faq/')
	
	template_dict = add_testimonials(template_dict)

	return render_to_response('pages/faq.html', template_dict, context_instance = RequestContext(request))
	
def detail(request, lang_code, prop_id):
	template_dict = generate_base_dict(lang_code, '/detail/')

	if request.method == 'POST' and 'property_ids' in request.POST:
		print request.POST['property_ids']
		template_dict['property_ids'] = request.POST['property_ids']
	else:
		print 'nincs benne'
	template_dict['curr_property_id'] = prop_id

	template_dict['property'] = Property.objects.filter(property_id = prop_id)[0]
	template_dict['property'].description = PropertyDescription.objects.filter(language__lang_code = lang_code, property__property_id = template_dict['property'].property_id)[0].description

	images = PropertyThumbnail.objects.filter(property__property_id = prop_id)
	template_dict['big_images'] = [sub(r'(.*/)([^/]+)', r'\1detail-big/\2', i.image.name) for i in images if match(r'.*(T|t)humbnail.*', i.image.name) == None][:5]
	template_dict['small_images'] = [sub(r'(.*/)([^/]+)', r'\1detail-big/\2', i.image.name) for i in images if match(r'.*(T|t)humbnail.*', i.image.name) == None][:5]
	
	template_dict = add_searchform(template_dict)
	template_dict = add_testimonials(template_dict)
	
	return render_to_response('pages/detail.html', template_dict, context_instance = RequestContext(request))

# Only dummy functions and classes below this point
class OfficeDummy():
	def __init__(self,staff):
		self.staff = staff


class TestimonialDummy():
	def __init__(self, thumbnail, address):
		self.thumbnail = thumbnail
		self.address = address
		
	def __str__(self):
		return str((self.thumbnail, self.address))