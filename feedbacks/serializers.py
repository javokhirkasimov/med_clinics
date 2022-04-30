from rest_framework import serializers
from .models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Feedback
        fields = '__all__'
