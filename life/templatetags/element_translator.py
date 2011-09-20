from django import template
from life.models import *

register = template.Library()

def get_text(parser, token):
	print 'token:', token.contents
	tag_name, element_id = token.split_contents()
	return  TranslatedTextNode(element_id, True)
	
class TranslatedTextNode(template.Node):
	
	def __init__(self, element_id, debug):
		self.element_id = element_id
		self.debug = debug
		
	def render(self, context):
		print 'context["curr_lang_code"]', context["curr_lang_code"]
		print 'self.element_id', self.element_id
		print 'query:', TextElementTranslation.objects.filter(language__lang_code=context['curr_lang_code'], element_name__element_name=self.element_id) 
		desired_text_element = TextElementTranslation.objects.filter(language__lang_code=context['curr_lang_code'], element_name__element_name=self.element_id)[0].element_text
		
		'''if self.debug:
			return '<span onclick="popup_translate_box()" mouseover="highlight_text()">' + desired_text_element + </span>
		else:
			return desired_text_element'''
		
		return desired_text_element

register.tag('gettext', get_text)