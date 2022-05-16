from rest_framework import generics
from .serializers import ClinicSerializer
from .models import Clinic


class ClinicsListView(generics.ListAPIView):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()
