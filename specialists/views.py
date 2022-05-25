from rest_framework import generics
from .serializers import SpecialistSerializer
from .models import Specialist
from feedbacks.serializers import FeedbackSerializer
from feedbacks.models import Feedback


class SpecialistListView(generics.ListAPIView):
    pagination_class = None
    serializer_class = SpecialistSerializer
    queryset = Specialist.objects.all()


class SpecialistRetrieveView(generics.RetrieveAPIView):
    serializer_class = SpecialistSerializer
    queryset = Specialist.objects.all()


class SpecialistFeedbacksListView(generics.ListAPIView):
    pagination_class = None
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        return Feedback.objects.filter(specialist_id=self.kwargs['pk'])
