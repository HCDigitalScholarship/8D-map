from django import forms
from map_app.models import *
from dal import autocomplete

from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticMapWidget

class PartnerSiteAdminForm(forms.ModelForm):
    class Meta:
        model = PartnerSite
        fields = "__all__"
        widgets = {
            'geom':GooglePointFieldWidget(settings={"GooglePointFieldWidget":(("zoom",8),)}),
        }


class PartnerSiteAdminStaticForm(forms.ModelForm):
    class Meta:
        model = PartnerSite
        fields = "__all__"
        widgets = {
            'geom':GoogleStaticMapWidget,
        }

class SearchForm(forms.ModelForm):
	search = forms.CharField(label='search', max_length=100, required=False)
	#site = forms.ModelChoiceField(queryset=PartnerSite.objects.all())
	class Meta:
		fields = ['area_of_interest', 'type_of_opportunity','language','region','subject', 'keywords']
		model = PartnerSite
