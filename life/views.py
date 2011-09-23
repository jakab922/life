from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from models import *

def generate_base_dict(lang_code, pagename):
	languages = [(langobj.lang_code, langobj.lang) for langobj in Language.objects.all()]
	
	for language in languages: # The current langauge need to be selected
		if language[0] == lang_code:
			languages.remove(language)
			languages = [language] + languages
			break
	
	return {'pagename': pagename, 'curr_lang_code': lang_code, 'curr_lang': Language.objects.filter(lang_code = lang_code)[0].lang, 'curr_flag': Language.objects.filter(lang_code = lang_code)[0].flag, 'languages': languages}
	

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
		
	template_dict['four_element'] = range(1,5)
	template_dict['three_element'] = range(1,4)
		
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
		
	template_dict['four_element'] = range(1,5)
	template_dict['three_element'] = range(1,4)
	if subpage == 'our_staff':
		template_dict['offices'] = [OfficeDummy(range(1,3)) for i in range(2)]
	
	return render_to_response('pages/about_us.html', template_dict, context_instance = RequestContext(request))
	
def index(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/')
	
	template_dict['four_element'] = [1,2,3,4]
	template_dict['three_element'] = [1,2,3]
	
	return render_to_response('pages/index.html', template_dict, context_instance = RequestContext(request))
	
def to_english(request):
	return redirect('/uk/')
	
def search(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/search/')
	
	template_dict['search_results'] = range(7)
	template_dict['three_element'] = range(1,4)
	
	return render_to_response('pages/search.html', template_dict, context_instance = RequestContext(request))
	
def landlords(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/landlords/')
	
	template_dict['previous_developments'] = [TestimonialDummy('/images/prev_dev_thumb1.jpg', 'Cadwell House, London SW13') for i in range(3)]
	template_dict['three_element'] = range(1,4)
	
	return render_to_response('pages/landlords.html', template_dict, context_instance = RequestContext(request))
	
def tenants(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/tenants/')
	
	template_dict['four_element'] = range(1,5)
	template_dict['three_element'] = range(1,4)
	
	return render_to_response('pages/tenants.html', template_dict, context_instance = RequestContext(request))

def buyers(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/buyers/')

	template_dict['four_element'] = range(1,5)
	template_dict['three_element'] = range(1,4)

	return render_to_response('pages/buyers.html', template_dict, context_instance = RequestContext(request))

def corporate(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/corporate/')

	template_dict['four_element'] = range(1,5)
	template_dict['three_element'] = range(1,4)

	return render_to_response('pages/corporate.html', template_dict, context_instance = RequestContext(request))
	
def currency_exchange(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/currency_exchange/')

	template_dict['three_element'] = range(1,4)

	return render_to_response('pages/corporate.html', template_dict, context_instance = RequestContext(request))
	
def faq(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/faq/')
	
	template_dict['three_element'] = range(1,4)

	return render_to_response('pages/faq.html', template_dict, context_instance = RequestContext(request))
	
def detail(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/detail/')
	
	template_dict['three_element'] = range(1,4)
	
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