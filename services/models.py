from django.db import models
from specialists.models import Specialist
from clinics.models import Clinic


class ServiceType(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=250)
    desc = models.TextField(null=True, blank=True)
    price = models.BigIntegerField()
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# class ClinicService(models.Model):
#     specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.service.title
