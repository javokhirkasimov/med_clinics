from django.db import models
from clients.models import Client
from services.models import ClinicService


class Appointment(models.Model):
    service = models.ManyToManyField(ClinicService)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
