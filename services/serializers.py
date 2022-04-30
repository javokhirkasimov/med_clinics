from rest_framework import serializers
from .models import Service
from specialists.serializers import SpecialistSerializer
from clinics.serializers import ClinicSerializer


class ServiceSerializer(serializers.ModelSerializer):
    service_type = serializers.CharField(source='service_type.title')
    specialist = SpecialistSerializer(read_only=True)
    clinic = ClinicSerializer(read_only=True)

    class Meta:
        model = Service
        fields = ['id', 'title', 'desc', 'price', 'service_type', 'specialist', 'clinic']
