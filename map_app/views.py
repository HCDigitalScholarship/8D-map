from django.shortcuts import render
from map_app.models import *

# Create your views here.

def index(request):
    sites = PartnerSite.objects.all()
    return render(request, 'index.html', { 'sites':sites })
