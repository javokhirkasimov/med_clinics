from rest_framework import serializers
from .models import Appointment
from clients.serializers import ClientSerializer
from clients.models import Client
from med_clinics.utils import bot


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
        text = "Appointment ID: {appointment_id}\n" \
               "Client:\n" \
               "    Full Name: {client_name}\n" \
               "    Medical Card: {client_medical_card}\n" \
               "    Contact: {client_contact}\n" \
               "    Address: {client_address}\n" \
               "Clinic:\n" \
               "    Clinic ID: {clinic_id}\n" \
               "    Title: {clinic_title}\n" \
               "Services:\n".format(
                        appointment_id=instance.id,
                        client_name=client.full_name,
                        client_medical_card=client.medical_card,
                        client_contact=client.contact,
                        client_address=client.address,
                        clinic_id=services[0].clinic.id,
                        clinic_title=services[0].clinic
                )

        for s in services:
            text += f'    {s.title}\n'
        text += f"Date: {validated_data['date_time']}"
        bot.send_message(text)
        return instance
