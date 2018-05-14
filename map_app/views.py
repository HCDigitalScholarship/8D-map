from django.shortcuts import render
from map_app.models import *
from map_app.forms import *
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		query = request.POST.get('search', None)
		if form.is_valid():
			sites = PartnerSite.objects.filter(description__icontains=query)
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

