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

	if 'property_ids' in template_dict:
		template_dict = add_map_details(template_dict)
		print "We've got some property ids"
	else:
		print "We have no property ids"
		template_dict['property_ids'] = []
		template_dict['property_coords'] = []

	return template_dict
	
def add_testimonials(template_dict):
	template_dict['testimonials'] = [(t.testimonial.name, t.testimonial.date, t.quote) for t in TestimonialTranslation.objects.filter(language__lang_code = template_dict['curr_lang_code'])]
	
	return template_dict
	
def add_staff(template_dict):
	template_dict['staff'] = StaffMember.objects.all()

	return template_dict

def add_map_details(template_dict):
	coords = []

	for prop_id in template_dict['property_ids']:
		print type(prop_id), prop_id
		ccord = PropertyCoordinate.objects.filter(property__property_id = prop_id)[0]
		print ccord
		coords.append(ccord.latitude)
		coords.append(ccord.longitude)

	template_dict['property_coords'] = coords
	return template_dict