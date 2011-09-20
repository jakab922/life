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
	

def landlord_services(request, service_name):
	if service_name not in ['property_management', 'tax_advice', 'furnishing', 'client_info', 'engagement_terms']:
		service_name = 'landlord_services' # put base in list and redirect to base if not in list...
		
	if service_name == 'property_management':
		selflink_text = 'Property Management'
	elif service_name == 'tax_advice':
		selflink_text = 'Tax Advice'
	elif service_name == 'furnishing':
		selflink_text = 'Furnitures Sales/Rental'
	elif service_name == 'client_info':
		selflink_text = 'Client Information'
	elif service_name == 'engagement_terms':
		selflink_text = 'Terms of Engagement'
	else:
		selflink_text = ''
		
	content_name = 'elements/' + service_name + '.html'
		
	return render_to_response('pages/landlord_services.html', {'service_name': service_name, 'content_name': content_name, 'selflink_text': selflink_text}, context_instance = RequestContext(request))
	
def city_guide(request, area):
	if area not in ['central']:
		area = 'all'
		
	content_name = 'elements/city_guide_content/' + area + '.html'
	
	if area == 'all':
		container_class = 'page guide'
	else:
		container_class = 'page guide area'
		
	return render_to_response('pages/city_guide.html', { 'area_name': area, 'content_name': content_name, 'container_class': container_class }, context_instance = RequestContext(request))

def about_us(request, subpage):
	if subpage not in ['recruitment', 'our_staff']:
		subpage = 'base'
		
	content_name = 'elements/about_us_content/' + subpage + '.html'

	if subpage in ['base', 'recruitment']:
		real_content_id = 'about'
	else:
		real_content_id = 'staff'
		
	if subpage == 'base':
		container_class = 'page about'
	elif subpage == 'recruitment':
		container_class = 'page about recruitment'
	else:
		container_class = 'page staff'
	
	return render_to_response('pages/about_us.html', {'subpage': subpage, 'content_name': content_name, 'real_content_id': real_content_id, 'container_class': container_class}, context_instance = RequestContext(request))
	
def index(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/')
	
	template_dict['four_element'] = [1,2,3,4]
	template_dict['three_element'] = [1,2,3]
	
	return render_to_response('pages/index.html', template_dict, context_instance = RequestContext(request))
	
def to_english(request):
	return redirect('/uk/')
	
def search(request):
	search_results = range(7)
	return render_to_response('pages/search.html', {'search_results': search_results}, context_instance = RequestContext(request))
	
def landlords(request):
	template_dict = generate_base_dict(lang_code, '/landlords/')
	
	