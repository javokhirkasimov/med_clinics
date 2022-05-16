from django.db import models


class Clinic(models.Model):
    title = models.CharField(max_length=250, null=True)
    image = models.ImageField(upload_to='clinic_photo', null=True)
    phone_num = models.CharField(max_length=15, null=True)
    region = models.CharField(max_length=250, null=True)
    district = models.CharField(max_length=250, null=True)
    street = models.CharField(max_length=250, null=True)
    home_num = models.CharField(max_length=15, null=True)
    lat_long = models.CharField(max_length=255, null=True)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return self.title
