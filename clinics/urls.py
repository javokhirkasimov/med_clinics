from django.urls import path
from .views import ClinicsListView

urlpatterns = [
    path('', ClinicsListView.as_view(), name='list-clinics'),
]
