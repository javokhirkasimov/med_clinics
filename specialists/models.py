from django.db import models


class Specialist(models.Model):
    full_name = models.CharField(max_length=250, null=True)
    specialization = models.CharField(max_length=550, null=True)
    contact = models.CharField(max_length=15, null=True)
