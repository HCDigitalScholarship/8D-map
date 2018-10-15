from django.contrib import admin
from django.contrib.gis import admin as geoadmin
from leaflet.admin import LeafletGeoAdmin

from django.contrib.gis.db import models as geomodels
from map_app.forms import *
from map_app.models import *

# Note: we are renaming the original Admin and Form as we import them!

from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

from django import forms

#We have to unregister the normal admin, and then reregister ours

#class PartnerSiteAdmin(LeafletGeoAdmin):
class PartnerSiteAdmin(admin.ModelAdmin):
    list_filter = ('name', 'area_of_interest')
    search_fields = ['name']
    autocomplete_fields = ['organization','haverford_office','contact','area_of_interest','language','region','subject','keywords','type_of_opportunity',]
    #formfield_overrides = {
    #    models.PointField: {"widget": GooglePointFieldWidget}
    #}

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = PartnerSiteAdminForm
        else:
            self.form = PartnerSiteAdminStaticForm
        return super(PartnerSiteAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(PartnerSite, PartnerSiteAdmin)
#geoadmin.site.register(PartnerSite, LeafletGeoAdmin)




class PersonAdmin(admin.ModelAdmin):
    search_fields = ['first_name','last_name',]

admin.site.register(Person, PersonAdmin)

class HaverfordOfficeAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(HaverfordOffice, HaverfordOfficeAdmin)

class PartnerOrganizationAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(PartnerOrganization, PartnerOrganizationAdmin)

class AreaOfInterestAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(AreaOfInterest, AreaOfInterestAdmin)

class LanguageAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Language, LanguageAdmin)

class RegionAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Region, RegionAdmin)

class SubjectAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Subject, SubjectAdmin)

class TypeOfOpportunityAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(TypeOfOpportunity, TypeOfOpportunityAdmin)

class KeywordAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Keyword, KeywordAdmin)
