from django.core.management.base import BaseCommand
from urllib import urlencode, urlopen, urlretrieve
from xml.etree.ElementTree import fromstring
from life.models import *
import re
from django.core.files import File
from time import sleep


class Command(BaseCommand):
	def update_properties(self):
		sock = urlopen('http://web.aspasia.net/pls/liferes/aspasia_search.xml', urlencode({'upw': '1467581F8E6F42D1BF0207B0A16964DE', 'de': 'RS', 'pf': 0, 'pt': 999999999, 'be': 0, 'pp': 100}))
		tree = fromstring(sock.read())
		sock.close()
	
		properties = []
		addresses = []
		descriptions = []
		images = []
		ext_pattern = re.compile(r'.*(\.[^\.]+)$')
	
		for property in tree.findall('houses/property'):
			p = {}
			p['property_id'] = property.find('id').text
			p['sale_type'] = 'S'
			p['branch'] = Branch.objects.filter(code = property.find('branch').text)[0]
			
			a = {}
			a['address'] = ', '.join([property.find('address/address' + str(i)).text for i in range(1,4) if property.find('address/address' + str(i)).text != None])
			a['city'] = 'London'
			a['postcode'] = property.find('address/postcode').text
			p['district'] = District.objects.filter(name = property.find('address/property_location').text)[0]
			
			p['price'] = property.find('property_summary/price').text
			p['bed_count'] = property.find('property_summary/beds').text
			p['bath_count'] = property.find('property_summary/baths').text
			p['reception_count'] = property.find('property_summary/receptions').text
			p['status_code'] = property.find('property_summary/status').text
			p['tenure_type'] = property.find('property_summary/freehold').text
			
			d = {}
			d['language'] = Language.objects.filter(lang_code = 'uk')[0]
			d['description'] = property.find('property_summary/long_description/para').text
			
			p['age'] = property.find('extra_info/prag_code').text
			p['setting'] = property.find('extra_info/prse_code').text
			if property.find('extra_info/prst_code').text != None:
				p['style'] = property.find('extra_info/prst_code').text
			else:
				p['style'] = 'NA'
			if property.find('extra_info/prty_code').text != None:
				p['type'] = property.find('extra_info/prty_code').text
			else:
				p['type'] = 'NA'
			if property.find('extra_info/prpa_code').text != None:
				p['parking'] = property.find('extra_info/prpa_code').text
			else:
				p['parking'] = 'NA'
			
			counter = 1
			i = []
			for picture in property.findall('images/*'):
				if picture.tag.startswith('picture'): # we only care about picture[0-9]+ tags
					i.append( (urlretrieve(picture.text)[0], '-'.join( [ p['property_id'], picture.attrib['type'], re.sub(r' ', r'_', picture.attrib['description'] ), "%02d" % counter ] ) + re.match(ext_pattern, picture.text).group(1) ) )
					sleep(5)
					counter += 1
			
			properties.append(p)
			addresses.append(a)
			descriptions.append(d)
			images.append({'i': i})
		
		# Need saving to PropertyDescription, PropertyThumbnail, Property and Addresses
		for c in range(len(properties)):
			properties[c]['address'] = Address(**addresses[c])
			properties[c]['address'].save()
			images[c]['property'] = descriptions[c]['property'] = Property(**properties[c])
			images[c]['property'].save()
			PropertyDescription(**descriptions[c]).save()
			for data in images[c]['i']:
				imfile = File(open(data[0]))
				thumb = PropertyThumbnail(property = images[c]['property'], image = imfile)
				thumb.image.save(data[1], imfile)
				thumb.save()		
	
	def handle(self, *args, **options):
		self.update_properties()