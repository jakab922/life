from django.core.management.base import BaseCommand
from urllib import urlencode, urlopen, urlretrieve
from xml.etree.ElementTree import fromstring
from life.models import *
import re
from django.db.models import ImageField
from time import sleep

class Command(BaseCommand):
	def bubba(self):
		sock = urlopen('http://web.aspasia.net/pls/liferes/aspasia_search.xml', urlencode({'upw': '1467581F8E6F42D1BF0207B0A16964DE', 'de': 'RS', 'pf': 0, 'pt': 999999999, 'be': 0, 'pp': 100}))
		tree = fromstring(sock.read())
		sock.close()
		
		c = 0
		for fim in tree.findall('houses/property/images/picture1'):
			a = urlretrieve(fim.text)
			print a
			c += 1
			if c > 2:
				break
		sleep(100)
		
	def handle(self, *args, **options):
		self.bubba()