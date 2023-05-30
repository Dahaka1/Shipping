from rest_framework import serializers
from .models import Cargo


class CargoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cargo
		fields = "__all__"

	def validate(self, attrs):
		instance = Cargo(**attrs)
		instance.clean()
		return attrs
