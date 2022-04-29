from django.contrib import admin
from .models import Service, ServiceType, ClinicService
# Register your models here.

admin.site.register(Service)
admin.site.register(ServiceType)
admin.site.register(ClinicService)
