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

