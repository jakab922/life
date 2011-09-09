from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template as dtt
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', dtt, {'template': 'empty.html'}),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
