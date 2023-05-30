from django.core.management import BaseCommand


class Command(BaseCommand):
	help = "Initializing default Location's objects"

	def handle(self, *args, **options):
		from locations.models import Location
		Location.locations_init()
