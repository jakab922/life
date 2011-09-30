from django.core.management.base import BaseCommand
from urllib import urlencode, urlopen
from xml.etree.ElementTree import fromstring
from life.models import *

class Command(BaseCommand):
	def update_branches(self):
		sock = urlopen('http://web.aspasia.net/pls/liferes/aspasia_lookup.branches')
		tree = fromstring(sock.read())
		sock.close()
		branch_dict = {'code': {'query': ['code']}, 'name': {'query': ['name']}, 'address': {'query': ['address1', 'address2']}, 'city': {'query': ['town']}, 'postcode': {'query': ['postcode']}, 'telephone': {'query': ['telephone']}, 'fax': {'query': ['fax']}, 'email': {'query': ['email']}}

		for record in tree.findall('record'):
			print ''
			for key in branch_dict.keys():
				curr = []
				for name in branch_dict[key]['query']:
					if record.find(name).text != None:
						curr.append(record.find(name).text)
				if len(curr) == 0:
					curr = ['']
				branch_dict[key]['value'] = ', '.join(curr)
			print branch_dict
			
			# If the address is new we are adding it.
			addresses = Address.objects.filter(address = branch_dict['address']['value'], postcode = branch_dict['postcode']['value'], city = 'London')
			if len(addresses) == 0:
				addresses = [Address(address = branch_dict['address']['value'], postcode = branch_dict['postcode']['value'], city = 'London')]
				addresses[0].save()
			
			# If the branch is new we are adding it.
			if len(Branch.objects.filter(code = branch_dict['code']['value'])) == 0:
				Branch(code = branch_dict['code']['value'], name = branch_dict['name']['value'], address = addresses[-1], phone = branch_dict['telephone']['value'], fax = branch_dict['fax']['value'], email = branch_dict['email']['value']).save()
		print ''
	
	def handle(self, *args, **options):
		self.update_branches()