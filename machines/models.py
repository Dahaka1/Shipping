from django.db import models
from locations.models import Location
from random import randrange, choice
from loguru import logger
from string import ascii_uppercase
from geopy.distance import geodesic


class Machine(models.Model):
	"""
	machine's ORModel
	"""
	uid = models.CharField(
		max_length=5,
		unique=True
	)
	location = models.ForeignKey(
		Location,
		on_delete=models.PROTECT,
		default=None,
		null=True
	)
	tonnage = models.PositiveSmallIntegerField(
		null=True
	)

	def __str__(self):
		return f"{self.uid}, tonnage: {self.tonnage}"

	@staticmethod
	def machines_init() -> None:
		existing_objects_amount = len(Machine.objects.all())
		amount_needed = 20
		if not existing_objects_amount:
			for _ in range(amount_needed):
				Machine.objects.create(
					uid=f"{randrange(1000, 10000)}{choice(ascii_uppercase)}",
					location=choice(Location.objects.all()),
					tonnage=randrange(1,1001)
				)
			logger.info(
				f"There are {amount_needed} {Machine.__class__} objects was created"
			)
		else:
			logger.info(
				f"There are {existing_objects_amount} {Machine.__class__} objects already exists"
			)

	def get_distance(self, geocode: tuple[float, float]) -> float:
		current_location = self.location.lat, self.location.lng
		return geodesic(current_location, geocode).miles

