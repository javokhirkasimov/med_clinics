from django.db import models


class Client(models.Model):
    full_name = models.CharField(max_length=250, null=True)
    medical_card = models.CharField(max_length=200, null=True)
    contact = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=350, null=True)

    def __str__(self):
        return self.full_name
