from django.db import models

class StaffMember(models.Model):
	name = models.CharField(max_length = 200)
	email = models.EmailField()
	thumbnail = models.ImageField(upload_to = 'images/thumbnails')
	language = models.ForeignKey('Language')
	creation_date = models.DateTimeField(auto_now_add = True)
	update_date = models.DateTimeField(auto_now = True)
	
	def __unicode__(self):
		return unicode((self.id, self.name))
		
class Language(models.Model):
	lang_code = models.CharField(max_length = 2, unique = True)
	lang = models.CharField(max_length = 50, unique = True)
	flag = models.ImageField(upload_to = 'images/flags')
	
	def __unicode__(self):
		return unicode(self.lang)
		
class Faq(models.Model):
	title = models.CharField(max_length = 200)
	question = models.CharField(max_length = 200)
	answer = models.TextField()
	
	def __unicode__(self):
		return unicode(self.title)
		
class Testimonial(models.Model):
	quote = models.TextField()
	name = models.CharField(max_length = 200)
	date = models.DateTimeField()
	
	def __unicode__(self):
		if len(self.quote) < 60:
			return unicode(self.quote)
		else:
			return unicode(self.quote[:60] + '...')
			
class TextElement(models.Model):
	element_name = models.CharField(max_length = 200)
	
	def __unicode__(self):
		return unicode(self.element_name)
		
class TextElementTranslation(models.Model):
	element_name = models.ForeignKey('TextElement')
	element_text = models.TextField()
	language = models.ForeignKey('Language')
	
	def __unicode__(self):
		return unicode((self.language, self.element_name))