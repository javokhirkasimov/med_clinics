from rest_framework import generics, filters
from .serializers import ClinicSerializer
from .models import Clinic
from services.serializers import ServiceSerializer
from services.models import Service
from specialists.serializers import SpecialistSerializer
from specialists.models import Specialist


class ClinicsListView(generics.ListAPIView):
    filter_backends = [filters.SearchFilter]
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()
    search_fields = [
        'title',
        'region',
        'district',
        'street'
    ]


class ClinicsRetrieveView(generics.RetrieveAPIView):
    serializer_class = ClinicSerializer
    queryset = Clinic.objects.all()


class ClinicsServicesListView(generics.ListAPIView):
    pagination_class = None
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return Service.objects.filter(clinic_id=self.kwargs['pk'])


class ClinicsSpecialistsListView(generics.ListAPIView):
    pagination_class = None
    serializer_class = SpecialistSerializer

    def get_queryset(self):
        return Specialist.objects.filter(clinic_id=self.kwargs['pk'])
    