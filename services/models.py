from django.db import models
from specialists.models import Specialist
from clinics.models import Clinic


class ServiceType(models.Model):
    title = models.CharField(max_length=250)


class Service(models.Model):
    title = models.CharField(max_length=250)
    price = models.BigIntegerField()
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)


class ClinicService(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
