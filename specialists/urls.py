from django.urls import path
from .views import SpecialistListView, SpecialistRetrieveView

urlpatterns = [
    path('', SpecialistListView.as_view(), name='list-specialist'),
    path('<int:pk>/', SpecialistRetrieveView.as_view(), name='detail-specialist'),
]
