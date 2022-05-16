from django.urls import path
from .views import ServiceListView, ServiceRetrieve

urlpatterns = [
    path('', ServiceListView.as_view(), name='service-list'),
    path('<int:pk>', ServiceRetrieve.as_view(), name='detail-list'),
]
