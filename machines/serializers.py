from rest_framework import serializers
from machines.models import Machine


class MachineSerializer(serializers.ModelSerializer):
	class Meta:
		model = Machine
		fields = "__all__"
		extra_kwargs = {"uid": {"required": False}}
