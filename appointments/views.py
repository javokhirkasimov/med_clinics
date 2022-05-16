from rest_framework import generics
from .serializers import AppointmentSerializer
from .models import Appointment


class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
