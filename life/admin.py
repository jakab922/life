from models import *
from django.contrib import admin

class StaffMemberAdmin(admin.ModelAdmin):
	list_display = ('name', 'email')
	list_filter = ('language',)
	ordering = ('name',)
	search_fields = ('name', 'language')

admin.site.register(StaffMember, StaffMemberAdmin)

class FaqAdmin(admin.ModelAdmin):
	list_display = ('name',)
	ordering = ('name',)
	search_fields = ('name',)

admin.site.register(Faq, FaqAdmin)

class FaqTranslationAdmin(admin.ModelAdmin):
	list_display = ('question',)
	ordering = ('question',)
	search_fields = ('question', 'answer')
	list_filter = ('language', 'faq')
	
admin.site.register(FaqTranslation, FaqTranslationAdmin)

class TestimonialAdmin(admin.ModelAdmin):
	list_display = ('quote_name',)
	search_fields = ('quote_name',)

admin.site.register(Testimonial, TestimonialAdmin)

class TestimonialTranslationAdmin(admin.ModelAdmin):
	list_display = ('__unicode__',)
	search_fields = ('quote',)
	list_filter = ('language', 'testimonial')

admin.site.register(TestimonialTranslation, TestimonialTranslationAdmin)

class LanguageAdmin(admin.ModelAdmin):
	search_fields = ('lang',)
	
admin.site.register(Language, LanguageAdmin)

class TextElementAdmin(admin.ModelAdmin):
	search_fields = ('element_name',)
	ordering = ('element_name',)
	
admin.site.register(TextElement, TextElementAdmin)

class TextElementTranslationAdmin(admin.ModelAdmin):
	list_display = ('element_name', 'language')
	list_filter = ('element_name', 'language')
	ordering = ('language', 'element_name')
	search_fields = ('language__lang', 'element_name__element_name')
	
admin.site.register(TextElementTranslation, TextElementTranslationAdmin)

class AddressAdmin(admin.ModelAdmin):
	list_display = ('address', 'city', 'postcode')
	ordering = ('address',)
	search_fields = ('address', 'city', 'postcode')
	list_filter = ('city',)
	
admin.site.register(Address, AddressAdmin)

class BranchAdmin(admin.ModelAdmin):
	list_display = ('code', 'name')
	ordering = ('code',)
	search_fields = ('code', 'name')
	
admin.site.register(Branch, BranchAdmin)

class CityPartAdmin(admin.ModelAdmin):
	list_display = ('cp_id', 'name',)
	ordering = ('name',)
	search_fields = ('name',)
	
admin.site.register(CityPart, CityPartAdmin)

class DistrictAdmin(admin.ModelAdmin):
	list_diplay = ('name', 'part')
	ordering = ('name',)
	search_fields = ('name', 'part')
	list_filter = ('part', )

admin.site.register(District, DistrictAdmin)

class PropertyDescriptionAdmin(admin.ModelAdmin):
	list_display = ('property', 'language')
	ordering = ('property',)
	search_fields = ('property', 'description', 'short_desc', 'language')
	list_filter = ('language', 'property')
	
admin.site.register(PropertyDescription, PropertyDescriptionAdmin)

class PropertyThumbnailAdmin(admin.ModelAdmin):
	list_display = ('property',)
	ordering = ('property',)
	search_fields = ('property',)
	
admin.site.register(PropertyThumbnail, PropertyThumbnailAdmin)

class PropertyCoordinateAdmin(admin.ModelAdmin):
	list_display = ('property','longitude', 'latitude')
	ordering = ('property',)
	search_fields = ('property', 'longitude', 'latitude')
	
admin.site.register(PropertyCoordinate, PropertyCoordinateAdmin)

class PropertyAdmin(admin.ModelAdmin):
	list_display = ('property_id', 'address', 'branch', 'sale_type')
	ordering = ('property_id',)
	search_fields = ('property', 'address', 'branch')
	list_filter = ('branch', 'district')
	
admin.site.register(Property, PropertyAdmin)