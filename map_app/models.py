from django.db import models
from django.contrib.gis.db import models
from djgeojson.fields import PointField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class ContactManager(models.Manager):
    def get_contact(self, contact):
        return self.filter(contact__icontains=contact)

class PartnerSite(models.Model):

    geom = PointField(null=True, blank=True)
    name = models.CharField(max_length=200, blank=True)
    organization = models.ManyToManyField('PartnerOrganization', blank=True)
    contact = models.ManyToManyField('Person', blank=True)
    haverford_office = models.ManyToManyField('HaverfordOffice', blank=True)
    description = RichTextUploadingField(blank=True)
    when_available = models.CharField(max_length=200, blank=True)
    type_of_opportunity = models.ManyToManyField('TypeOfOpportunity', blank=True)
    area_of_interest = models.ManyToManyField('AreaOfInterest', blank=True)
    language = models.ManyToManyField('Language', blank=True)
    region = models.ManyToManyField('Region', blank=True)
    subject = models.ManyToManyField('Subject', blank=True)
    keywords = models.ManyToManyField('Keyword', blank=True)

    @property
    def popupContent(self):
        if self.contact.first():

            return '<br><b>{}</b><br><p>{}</p><br><p>Contact: <a href="mailto:{}">{}</a></p>'.format(
            self.name,
            self.description,
            self.contact.first().email,
            self.contact.first().name)
        else:
            return '<br><b>{}</b><br><p>{}</p>'.format(
            self.name,
            self.description)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length= 200, blank=True)
    profile = RichTextField(blank=True)

    @property
    def name(self):
        return ''.join(
            [self.first_name,' ', self.last_name,])

    def __str__(self):
        return self.name

class HaverfordOffice(models.Model):
    name = models.CharField(max_length=200, blank=True, help_text="Name of office on campus that maintains this partnership.")
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name

class PartnerOrganization(models.Model):
    name = models.CharField(max_length=200, blank=True, help_text="Name of the partner organization.")
    address = models.CharField(max_length=200, blank=True)
    sites = models.ManyToManyField(PartnerSite, blank=True)
    contact = models.ManyToManyField(Person, blank=True)
    website = models.URLField(max_length=200, blank=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name

class AreaOfInterest(models.Model):
    name = models.CharField(max_length=200, blank=True, help_text="General categories of interest, such as education, human rights or sustainable agriculture.")

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=200, blank=True, help_text="Relevant academic disciplines or majors")
    def __str__(self):
        return self.name

class TypeOfOpportunity(models.Model):
    name = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name

class Keyword(models.Model):
    name = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name
