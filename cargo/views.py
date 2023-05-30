from .models import Cargo
from rest_framework import viewsets
from .serializers import CargoSerializer
from locations.models import Location
from rest_framework.response import Response
from django.forms.models import model_to_dict


class CargoViewSet(viewsets.ModelViewSet):
	queryset = Cargo.objects.all()
	serializer_class = CargoSerializer

	# def get_queryset(self):
	# 	pass

	def create(self, request, *args, **kwargs):
		context = request.data
		pickup_zip, delivery_zip = context.pop("pickup_zip", None), context.pop("delivery_zip", None)
		if not any(arg is None for arg in (pickup_zip, delivery_zip)):
			try:
				pickup_location, delivery_location = Location.objects.get(zip=pickup_zip), \
					Location.objects.get(zip=delivery_zip)
			except:
				return Response({"error": "Locations wasn't founded by current zip-codes"})

			context["pickup_location"] = pickup_location.pk
			context["delivery_location"] = delivery_location.pk

			serializer = CargoSerializer(data=context)
			serializer.is_valid(raise_exception=True)
			serializer.save()
			print(serializer.data)
			return Response(serializer.data)
		else:
			return Response({"error": "Needs for pickup- and delivery zip codes"})

	def list(self, request, *args, **kwargs):
		out = []
		units = self.queryset
		for unit in units:
			raw_model = model_to_dict(unit)
			raw_model.setdefault("machines_nearby", unit.nearest_machines_amount())
			out.append(raw_model)
		return Response({"data": out})

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		context = serializer.data
		context.setdefault("machines_distance", instance.get_machines(list_type="all"))
		return Response(context)
