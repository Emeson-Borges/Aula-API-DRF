from django.urls import path
from .views import EstudantesListCreate, EstudantesRetrieveUpdateDestroy

urlpatterns = [
    path('estudantes/', EstudantesListCreate.as_view(), name='student-list-create'),
    path('estudantes/<int:pk>/', EstudantesRetrieveUpdateDestroy.as_view(), name='student-detail'),
]
