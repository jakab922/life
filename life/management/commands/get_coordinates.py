from django.core.management.base import BaseCommand
from urllib import urlencode, urlopen
from life.models import Property, PropertyCoordinate
from json import loads
from re import match


class Command(BaseCommand):
	def get_coordinates(self):
		base_address = 'http://maps.googleapis.com/maps/api/geocode/json?'
		london_coords = {'lat': 51.50015240, 'lng': -0.12623620}
		properties = Property.objects.all()

		addresses = []
		for property in properties:
			curr_addresses = []
			for address in property.address.address.split(','):
				if(match(r'[0-9]+(?: [a-zA-Z]+)+', address) != None):
					curr_addresses.append(address + ', london')
					
			curr_addresses.append(property.address.postcode + ', london')
			addresses.append(curr_addresses)
			
		for i in range(len(addresses)):
			big_found = False
			for address in addresses[i]:
				results = loads(urlopen(base_address + urlencode({'sensor': 'false', 'address': address})).read())['results']
				
				found = False

				if len(results) != 0:
					for result in results:
						if abs(float(result['geometry']['location']['lat']) - london_coords['lat']) < 0.3 and abs(float(result['geometry']['location']['lng']) - london_coords['lng']) < 0.3:
							pc = PropertyCoordinate(longitude = result['geometry']['location']['lng'], latitude = result['geometry']['location']['lat'], property = properties[i])
							pc.save()
							print properties[i].address.address, result['geometry']['location']
							found = True
							break
				if found:
					big_found = True
					break
			if not big_found:
				print 'Not found'

	def handle(self, *args, **options):
		self.get_coordinates()