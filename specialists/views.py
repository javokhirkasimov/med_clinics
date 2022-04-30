from rest_framework import generics
from .serializers import SpecialistSerializer
from .models import Specialist


class SpecialistListView(generics.ListAPIView):
    serializer_class = SpecialistSerializer
    queryset = Specialist.objects.all()


class SpecialistRetrieveView(generics.RetrieveAPIView):
    serializer_class = SpecialistSerializer
    queryset = Specialist.objects.all()
