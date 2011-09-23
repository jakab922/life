from django.core.management.base import BaseCommand
from life.models import *
from xml.etree.ElementTree import fromstring
from urllib import urlopen

class Command(BaseCommand):
	def load_locations(self):
		sock = urlopen('http://web.aspasia.net/pls/liferes/aspasia_lookup.locations?xm=Y')
		tree = fromstring(sock.read())
		
		for record in tree.findall('record'):
			print '---'
			print record.find('location').text
			for town in record.findall('towns'):
				print ', '.join([town.find('town').text, town.find('site').text, town.find('county').text])
	
	def handle(self, *args, **options):
		self.load_locations()
		
	
		