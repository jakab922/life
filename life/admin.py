from models import *
from django.contrib import admin

class FaqAdmin(admin.ModelAdmin):
	list_display = ('title', 'question')
	ordering = ('title',)
	search_fields = ('title', 'question')

admin.site.register(Faq, FaqAdmin)

class StaffMemberAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'language')
	list_filter = ('language',)
	ordering = ('name',)
	search_fields = ('name', 'language')

admin.site.register(StaffMember, StaffMemberAdmin)

class TestimonialAdmin(admin.ModelAdmin):
	list_display = ('__unicode__',)
	search_fields = ('quote',)

admin.site.register(Testimonial, TestimonialAdmin)

class LanguageAdmin(admin.ModelAdmin):
	search_fields = ('lang',)
	
admin.site.register(Language, LanguageAdmin)

class TextElementAdmin(admin.ModelAdmin):
	list_display = ('element_name', 'language')
	list_filter = ('element_name', 'language')
	ordering = ('language',)
	search_fields = ('element_name', 'language')
	
admin.site.register(TextElement, TextElementAdmin)