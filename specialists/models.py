from django.db import models
from django.contrib.postgres.fields import ArrayField


class Education(models.Model):
    institution = models.CharField(max_length=500, null=True)
    speciality = models.CharField(max_length=500, null=True)
    finished = models.DateField()

    def __str__(self):
        return self.institution


class Specialist(models.Model):
    full_name = models.CharField(max_length=250, null=True)
    specialization = models.CharField(max_length=550, null=True)
    contact = models.CharField(max_length=15, null=True)
    photo = models.ImageField(upload_to='specialist_photo', null=True)
    experience = models.IntegerField(null=True)
    skills = ArrayField(
        models.CharField(max_length=255, blank=True),
        size=10,
        null=True
    )
    education = models.ManyToManyField(Education)

    def __str__(self):
        return self.full_name
