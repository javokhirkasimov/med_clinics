from rest_framework import generics, filters
from .serializers import ClinicSerializer
from .models import Clinic


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
