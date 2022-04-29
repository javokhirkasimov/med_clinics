from django.db import models


class ServiceType(models.Model):
    title = models.CharField(max_length=250)


class Service(models.Model):
    title = models.CharField(max_length=250)
    price = models.BigIntegerField()
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
