"""sourcebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from map_app import views
from map_app.models import *
from map_app.views import *
from django.conf.urls import include
from djgeojson.views import GeoJSONLayerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('data/', GeoJSONLayerView.as_view(model=PartnerSite, properties=('geom', 'description','name')), name='data'),
    #path('<site>', views.site, name='site'),
    path('autocomplete/', SiteAutocomplete.as_view(), name='autocomplete'),
]
