from django.db import models
from clients.models import Client
from services.models import Service


class Appointment(models.Model):
    service = models.ManyToManyField(Service)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment {self.created_at}"
