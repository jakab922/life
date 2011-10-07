from django.shortcuts import render_to_response, redirect
from life.views.aux import *

def index(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/')
	
	template_dict = add_searchform(template_dict)
	template_dict = add_staff(template_dict)
	template_dict = add_testimonials(template_dict)
	
	return render_to_response('pages/index.html', template_dict, context_instance = RequestContext(request))
	
def to_english(request):
	return redirect('/uk/')