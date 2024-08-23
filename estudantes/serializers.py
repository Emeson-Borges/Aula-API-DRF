from rest_framework import serializers
from .models import Estudantes

class EstudantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudantes
        fields = '__all__'
