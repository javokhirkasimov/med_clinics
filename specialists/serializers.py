from rest_framework import serializers
from .models import Specialist, Education
from feedbacks.serializers import FeedbackSerializer
from feedbacks.models import Feedback
from services.models import Service


class SpecialistServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class SpecialistSerializer(serializers.ModelSerializer):
    education = EducationSerializer(many=True)
    feedbacks = serializers.SerializerMethodField(read_only=True)
    services = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Specialist
        fields = [
            'id',
            'full_name',
            'specialization',
            'contact',
            'photo',
            'experience',
            'skills',
            'education',
            'feedbacks',
            'services'
        ]

    def get_feedbacks(self, obj):
        feedbacks = Feedback.objects.filter(specialist_id=obj.id)
        return FeedbackSerializer(feedbacks, many=True).data

    def get_services(self, obj):
        services = Service.objects.filter(specialist_id=obj.id)
        return SpecialistServicesSerializer(services, many=True).data
