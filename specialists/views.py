from rest_framework import generics
from .serializers import SpecialistSerializer
from .models import Specialist


class SpecialistListCreateView(generics.ListCreateAPIView):
    serializer_class = SpecialistSerializer
    queryset = Specialist.objects.all()


class SpecialistRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SpecialistSerializer
    queryset = Specialist.objects.all()
