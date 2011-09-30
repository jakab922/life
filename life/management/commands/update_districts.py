from django.core.management.base import BaseCommand
from urllib import urlopen
from xml.etree.ElementTree import fromstring
from life.models import *


class Command(BaseCommand):
	def update_city_parts(self):
		sock = urlopen('http://web.aspasia.net/pls/liferes/aspasia_lookup.locations?xm=Y')
		tree = fromstring(sock.read())
		sock.close()
		
		for record in tree.findall('record'):
			cp = CityPart.objects.filter(cp_id = record.find('towns/town_id').text)[0]
			District(name = record.find('location').text, part = cp).save()
	
	def handle(self, *args, **options):
		self.update_city_parts()