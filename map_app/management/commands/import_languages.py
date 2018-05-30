import csv 
from map_app.models import *
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
	help = "Import organizations from csv"
	def handle(self, *args, **options):
		with open('/tmp/languages.txt') as f:
			lines = f.readlines()
			for row in lines:
				print(row)
				Language.objects.update_or_create(
					name = row)
