from rest_framework import generics
from .serializers import FeedbackSerializer
from .models import Feedback


class FeedbackListCreateView(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        return Feedback.objects.filter(active=True)
