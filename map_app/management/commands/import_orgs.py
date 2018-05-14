import csv 
from map_app.models import *
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
	help = "Import organizations from csv"
	def handle(self, *args, **options):
		with open('/tmp/map.csv') as f:
				for row in csv.DictReader(f, skipinitialspace=True):
					print(row)
					PartnerOrganization.objects.update_or_create(
						name = row['Organization_Information_Name_of_Organization'],
						address = row['Street_Address'],
						website = row['Organization_Information_Website'])
