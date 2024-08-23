from rest_framework import generics
from .models import Estudantes
from .serializers import EstudantesSerializer

class EstudantesListCreate(generics.ListCreateAPIView):
    queryset = Estudantes.objects.all()
    serializer_class = EstudantesSerializer

class EstudantesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudantes.objects.all()
    serializer_class = EstudantesSerializer
