from django.urls import path
from .views import (
    ClinicsListView,
    ClinicsRetrieveView,
    ClinicsServicesListView,
    ClinicsSpecialistsListView
)

urlpatterns = [
    path('', ClinicsListView.as_view(), name='list-clinics'),
    path('<int:pk>', ClinicsRetrieveView.as_view(), name='detail-clinics'),
    path('<int:pk>/services', ClinicsServicesListView.as_view(), name='clinic-services'),
    path('<int:pk>/specialists', ClinicsSpecialistsListView.as_view(), name='clinc-specialists')
]
