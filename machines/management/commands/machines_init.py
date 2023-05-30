from django.core.management import BaseCommand


class Command(BaseCommand):
	help = "Initializing default Machine's objects"

	def handle(self, *args, **options):
		from machines.models import Machine
		Machine.machines_init()
