from django.db import models
from django.contrib.gis.db import models
from djgeojson.fields import PointField
from ckeditor.fields import RichTextField

class PartnerSite(models.Model):

    geom = PointField(null=True, blank=True)
    description = RichTextField()
    picture = models.ImageField()
    name = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name

    @property
    def popupContent(self):
      return '<img src="{}" /><p><{}</p>'.format(
          self.picture.url,
          self.description)

