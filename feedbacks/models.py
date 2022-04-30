from django.db import models
from specialists.models import Specialist


class Feedback(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250, null=True)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}-Active: {self.active}"
