from django.shortcuts import render_to_response, redirect
from life.views.aux import *
from life.models import Property, PropertyCoordinate, PropertyDescription, PropertyThumbnail
from re import sub, match

def detail(request, lang_code, prop_id):
	template_dict = generate_base_dict(lang_code, '/detail/')

	if request.method == 'POST' and 'property_ids' in request.POST:
		template_dict['property_ids'] = parse_json(request.POST['property_ids'])

	template_dict['curr_property_id'] = prop_id
	template_dict['curr_property_coord'] = [PropertyCoordinate.objects.filter(property__property_id = prop_id)[0].latitude, PropertyCoordinate.objects.filter(property__property_id = prop_id)[0].longitude] 

	template_dict['property'] = Property.objects.filter(property_id = prop_id)[0]
	template_dict['property'].description = PropertyDescription.objects.filter(language__lang_code = lang_code, property__property_id = template_dict['property'].property_id)[0].description

	images = PropertyThumbnail.objects.filter(property__property_id = prop_id)
	template_dict['big_images'] = [sub(r'(.*/)([^/]+)', r'\1detail-big/\2', i.image.name) for i in images if match(r'.*(T|t)humbnail.*', i.image.name) == None][:5]
	template_dict['small_images'] = [sub(r'(.*/)([^/]+)', r'\1detail-big/\2', i.image.name) for i in images if match(r'.*(T|t)humbnail.*', i.image.name) == None][:5]
	
	template_dict = add_searchform(template_dict)
	template_dict = add_testimonials(template_dict)
	
	return render_to_response('pages/detail.html', template_dict, context_instance = RequestContext(request))