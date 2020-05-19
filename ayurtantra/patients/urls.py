from django.urls import path
from .views import PatientListView, PatientUpdateView, PatientDetailView, PatientDeleteView, PatientCreateView

urlpatterns = [
    path('',PatientListView.as_view(), name = 'patient_list'),
    path('<int:pk>/delete/', PatientDeleteView.as_view(), name='patient_delete'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('<int:pk>/edit/', PatientUpdateView.as_view(), name='patient_edit'),
    path('new/', PatientCreateView.as_view(), name='patient_new'),
]