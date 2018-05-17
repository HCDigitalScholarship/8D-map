from dal import autocomplete
from django.shortcuts import render
from map_app.models import *
from map_app.forms import *
from django.shortcuts import get_object_or_404
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

# Create your views here.

def index(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		query = request.POST.get('search', None)
		print(request.POST)
		if form.is_valid():
			sites = PartnerSite.objects.annotate(search=SearchVector('name','area_of_interest__name')).filter(search=query)
			#sites = PartnerSite.objects.filter(description__icontains=query, name__icontains=query, area_of_interest__name=query)
			context  = {'sites':sites, 'form':form}
			return render(request, 'index.html', context)
		else:
			print(form.errors)
	else:
		sites = PartnerSite.objects.all()

		form = SearchForm()
		return render(request, 'index.html', {'sites':sites, 'form':form})

def site(request, site):
	site = get_object_or_404(PartnerSite, name=site)
	return render(request, 'site.html', {'site':site})



class SiteAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        qs = PartnerSite.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

