from django.urls import path
from .views import SpecialistListView, SpecialistRetrieveView, SpecialistFeedbacksListView

urlpatterns = [
    path('', SpecialistListView.as_view(), name='list-specialist'),
    path('<int:pk>/', SpecialistRetrieveView.as_view(), name='detail-specialist'),
    path('<int:pk>/feedbacks', SpecialistFeedbacksListView.as_view(), name='specialist-feedbacks')
]
