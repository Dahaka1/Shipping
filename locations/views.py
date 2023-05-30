from .models import Location
from rest_framework import generics
from .serializers import LocationSerializer


class LocationAPIView(generics.ListAPIView):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer
