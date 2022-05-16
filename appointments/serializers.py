from rest_framework import serializers
from .models import Appointment
from clients.serializers import ClientSerializer
from clients.models import Client


class AppointmentSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Appointment
        fields = ['service', 'client', 'date_time']
        extra_kwargs = {
            'service': {'required': True},
            'date_time': {'required': True}
        }

    def create(self, validated_data):
        client = Client.objects.create(**validated_data['client'])
        instance = Appointment.objects.create(
            client=client,
            date_time=validated_data['date_time']
        )
        services = validated_data['service']
        for s in services:
            instance.service.add(s)
        return instance
