from rest_framework import generics
from .serializers import ClientSerializer
from.models import Client


class ClientListView(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
