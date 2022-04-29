from django.urls import path
from .views import SpecialistListCreateView

urlpatterns = [
    path('', SpecialistListCreateView.as_view(), name='list-specialist'),
]
