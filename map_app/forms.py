from django import forms
from map_app.models import *


class SearchForm(forms.ModelForm):
	search = forms.CharField(label='search', max_length=100)
	class Meta:
		fields = ['name','area_of_interest','language','region','subject', 'keywords']
		model = PartnerSite

