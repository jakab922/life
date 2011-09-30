from django.core.management.base import BaseCommand
from urllib import urlopen
from xml.etree.ElementTree import fromstring
from life.models import *


class Command(BaseCommand):
	def update_city_parts(self):
		sock = urlopen('http://web.aspasia.net/pls/liferes/aspasia_lookup.towns?xm=Y')
		tree = fromstring(sock.read())
		sock.close()
		
		for record in tree.findall('record'):
			CityPart(cp_id = record.find('town_id').text, name = record.find('town').text).save()
	
	def handle(self, *args, **options):
		self.update_city_parts()