import geopy.location
from django.db import models
from csv import DictReader
from loguru import logger
from django.conf import settings


class Location(models.Model):
	"""
	location's ORModel
	"""
	city = models.CharField(
		max_length=50
	)
	state = models.CharField(
		max_length=50
	)
	zip = models.CharField(
		max_length=9
	)
	lat = models.FloatField()
	lng = models.FloatField()

	def __str__(self):
		return f"Location ID:{self.pk}, {self.city, self.state, self.zip, self.lat, self.lng}"

	def raw(self) -> tuple:
		out = self.lat, self.lng
		return tuple(out)

	@staticmethod
	def locations_init() -> None:
		file = open(settings.STATIC_LOCATIONS_SOURCE, encoding='utf-8')
		source = list(DictReader(file))
		if not Location.objects.all().exists():
			for location in source:
				Location.objects.create(
					city=location["city"],
					state=location["state_name"],
					zip=location["zip"],
					lat=location["lat"],
					lng=location["lng"]
				)
			logger.info(
				f"There are {len(source)} {Location.__class__} objects was created"
			)
		else:
			existing_objects_amount = len(Location.objects.all())
			logger.info(
				f"There are {existing_objects_amount} {Location.__class__} objects already exists"
			)
		file.close()

	# def geocode(self) -> geopy.location.Location:
	# 	geolocator = settings.GEOLOCATOR
	# 	location = geolocator.reverse(f"{self.lat}, {self.lng}")
	# 	return location
