from rest_framework import generics
from .serializers import AppointmentSerializer
from .models import Appointment


class AppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
