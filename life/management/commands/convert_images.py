from django.core.management.base import BaseCommand
import settings
from os import listdir
from re import match
from subprocess import call

class Command(BaseCommand):
	def convert_images(self):
		basedir = settings.ProjectDir + '/life/media/images/properties/'
		images = [f for f in listdir(basedir) if match(r'.*(jpe?g|png|gif|bmp)', f) != None]
		no_thumbs = [i for i in images if match(r'.*(t|T)humbnail.*', i) == None]
		
		# Scaling for the search page
		for image in images:
			call('convert {0} -background white -gravity center -resize {1} -extent {1} {2}'.format(basedir + image, '225x140', basedir + 'searchpage/' + image).split(' '))
			print 'Saved image', image, 'for searchpage' 

		# Scaling for the small images on detail page
		for image in no_thumbs:
			call('convert {0} -background white -gravity center -resize {1} -extent {1} {2}'.format(basedir + image, '137x85', basedir + 'detail-small/' + image).split(' '))
			print 'Saved image', image, 'for detail page(small)'
			
		# Scaling for the large images on the detail page
		for image in no_thumbs:
			call('convert {0} -background white -gravity center -resize {1} -extent {1} {2}'.format(basedir + image, '698x419', basedir + 'detail-big/' + image).split(' '))
			print 'Saved image', image, 'for detail page(big)'

	def handle(self, *args, **options):
		self.convert_images()