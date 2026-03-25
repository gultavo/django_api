from rest_framework import serializers
from .models import Estudantes, Cursos, Matriculas

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudantes
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matriculas
        fields = '__all__'