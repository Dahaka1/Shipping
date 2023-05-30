from .models import Machine
from rest_framework import viewsets
from .serializers import MachineSerializer
from rest_framework.response import Response
from locations.models import Location


class MachineViewSet(viewsets.ModelViewSet):
	queryset = Machine.objects.all()
	serializer_class = MachineSerializer

	def update(self, request, *args, **kwargs):
		instance = self.get_object()
		data = request.data
		location_zip = data.pop("zip", None)
		if not location_zip is None:
			try:
				location = Location.objects.get(zip=location_zip)
			except:
				return Response({"error": "Location wasn't founded by current zip-code"})
			data.setdefault("location", location.pk)
			serializer = self.get_serializer(instance, data=data, partial=False)  # disabled patch query
			serializer.is_valid(raise_exception=True)
			self.perform_update(serializer)

			if getattr(instance, '_prefetched_objects_cache', None):
				instance._prefetched_objects_cache = {}

			return Response(serializer.data)
		else:
			return Response({"error": "There is no needed location zip in request"})
