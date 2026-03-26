from rest_framework import serializers
from .models import Estudantes, Cursos, Matriculas

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudantes
        fields = ['id', 'nome', 'email']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = ['id', 'nome', 'quant_semestres', 'vagas']

class MatriculaSerializer(serializers.ModelSerializer):

    estudante = serializers.ReadOnlyField(source='estudante.nome')

    curso = serializers.ReadOnlyField(source='curso.nome')

    class Meta:
        model = Matriculas
        fields = ['id', 'estudante', 'curso', 'data_matricula']