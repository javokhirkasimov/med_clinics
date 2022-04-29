from django.db import models


class Clinic(models.Model):
    title = models.CharField(max_length=250, null=True)
    phone_num = models.CharField(max_length=15, null=True)
    region = models.CharField(max_length=250, null=True)
    district = models.CharField(max_length=250, null=True)
    street = models.CharField(max_length=250, null=True)
    home_num = models.CharField(max_length=15, null=True)
    open_time = models.TimeField()
    close_time = models.TimeField()
