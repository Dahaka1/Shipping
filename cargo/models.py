from typing import Optional

from django.db import models
from rest_framework.exceptions import ValidationError
from machines.models import Machine
from locations.models import Location
from geopy.distance import geodesic


class Cargo(models.Model):
	pickup_location = models.ForeignKey(
		Location,
		on_delete=models.PROTECT,
		default=None,
		null=True,
		related_name='%(class)s_pickup_location'
	)
	delivery_location = models.ForeignKey(
		Location,
		on_delete=models.PROTECT,
		default=None,
		null=True,
		related_name='%(class)s_delivery_location'
	)
	weight = models.PositiveSmallIntegerField()
	description = models.TextField(
		max_length=500,
		null=True,
		default=None,
		blank=True
	)

	def __str__(self):
		return f"CARGO ID:{self.pk}, PICKUP: {self.pickup_location}, " \
			   f"DELIVERY: {self.delivery_location}, WEIGHT: {self.weight}, " \
			   f"DESCRIPTION: {self.description}"

	def nearest_machines_amount(self) -> int:
		machines = self.get_machines(list_type="nearby")
		return len(machines) if not machines is None else 0

	def clean(self):
		if self.weight > 1000:
			raise ValidationError("Weight must be less than 1000")

	def get_machines(self, list_type: str) -> Optional[list[Machine]]:
		"""
		:param list_type: nearby/all
		"""
		machines = Machine.objects.all()
		current_location = self.pickup_location.raw()
		out = []
		for machine in machines:
			if list_type == "nearby":
				machine_location = machine.location.raw()
				distance = geodesic(current_location, machine_location).miles
				if distance <= 450:
					out.append(machine)
			elif list_type == "all":
				current_distance = machine.get_distance(current_location)
				out.append({machine.pk: current_distance})
		if any(out):
			return out

