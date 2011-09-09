from django.db import models

class StaffMember(models.Model):
	name = models.CharField(max_length = 200)
	email = models.EmailField()
	thumbnail = models.ImageField(upload_to = 'img/thumbnails')
	language = models.ForeignKey('Language')
	creation_date = models.DateTimeField(auto_now_add = True)
	update_date = models.DateTimeField(auto_now = True)
	
	def __unicode__(self):
		return unicode((self.id, self.name))
		
class Language(models.Model):
	lang = models.CharField(max_length = 50, unique = True)
	
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
	element_text = models.TextField()
	language = models.ForeignKey('Language')
	
	def __unicode__(self):
		return unicode((self.element_name, self.element_text))
