from django.contrib import admin
from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin

from map_app.models import *

# Note: we are renaming the original Admin and Form as we import them!

from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

from django import forms

#We have to unregister the normal admin, and then reregister ours
admin.site.register(PartnerSite, LeafletGeoAdmin)

class PersonAdmin(admin.ModelAdmin):
    pass 
admin.site.register(Person, PersonAdmin)

class HaverfordOfficeAdmin(admin.ModelAdmin):
    pass
admin.site.register(HaverfordOffice, HaverfordOfficeAdmin)

class PartnerOrganizationAdmin(admin.ModelAdmin):
    pass
admin.site.register(PartnerOrganization, PartnerOrganizationAdmin)

class AreaOfInterestAdmin(admin.ModelAdmin):
    pass
admin.site.register(AreaOfInterest, AreaOfInterestAdmin)

class LanguageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Language, LanguageAdmin)

class RegionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Region, RegionAdmin)

class SubjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(Subject, SubjectAdmin)

class TypeOfOpportunityAdmin(admin.ModelAdmin):
    pass
admin.site.register(TypeOfOpportunity, TypeOfOpportunityAdmin)

class KeywordAdmin(admin.ModelAdmin):
    pass
admin.site.register(Keyword, KeywordAdmin)
