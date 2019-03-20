from datetime import datetime
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
		language = request.POST.get('language', None)
		greeting = 'no'
		print(request.POST)
		print(language)
		if form.is_valid():
			if query == '':
				sites = PartnerSite.objects.all()
			else:
				sites = PartnerSite.objects.annotate(search=SearchVector('name','description','area_of_interest__name','language__name','organization__name','contact__first_name','contact__last_name','region__name','subject__name','keywords__name',)).filter(search=query)
				#sites = PartnerSite.objects.filter(description__icontains=query, name__icontains=query, area_of_interest__name=query)
			context  = {'sites':sites, 'form':form, 'greeting':greeting}
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
        qs = Language.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

def current(request):
        if request.method == 'POST':
                form = SearchForm(request.POST)
                query = request.POST.get('search', None)
                language = request.POST.get('language', None)
                print(request.POST)
                print(language)
                if form.is_valid():
                        if query == '':
                                sites = PartnerSite.objects.all()
                        else:
                            sites = PartnerSite.objects.annotate(search=SearchVector('name','description','area_of_interest__name','language__name','organization__name','contact__first_name','contact__last_name','region__name','subject__name','keywords__name',)).filter(search=query).filter(end_date__gt=datetime.now())
                            #sites = PartnerSite.objects.filter(description__icontains=query, name__icontains=query, area_of_interest__name=query)
                        context  = {'sites':sites, 'form':form}
                        return render(request, 'index.html', context)
                else:
                        print(form.errors)
        else:
                sites = PartnerSite.objects.filter(end_date__gt=datetime.now())

                form = SearchForm()
                return render(request, 'index.html', {'sites':sites, 'form':form})


def philly(request):
        if request.method == 'POST':
                form = SearchForm(request.POST)
                query = request.POST.get('search', None)
                language = request.POST.get('language', None)
                print(request.POST)
                print(language)
                if form.is_valid():
                        if query == '':
                                sites = PartnerSite.objects.all()
                        else:
                                sites = PartnerSite.objects.annotate(search=SearchVector('name','description','area_of_interest__name','language__name','organization__name','contact__first_name','contact__last_name','region__name','subject__name','keywords__name',)).filter(search=query)
                                #sites = PartnerSite.objects.filter(description__icontains=query, name__icontains=query, area_of_interest__name=query)
                        context  = {'sites':sites, 'form':form}
                        return render(request, 'philly.html', context)
                else:
                        print(form.errors)
        else:
                sites = PartnerSite.objects.all()

                form = SearchForm()
                return render(request, 'philly.html', {'sites':sites, 'form':form})
