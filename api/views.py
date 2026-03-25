from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Estudantes, Cursos, Matriculas
from .serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer

class EstudantesViewSet(viewsets.ModelViewSet):
    queryset = Estudantes.objects.all()
    serializer_class = EstudanteSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    filterset_fields = ['nome', 'email']
    
    search_fields = ['nome', 'email']

    ordering_fields = ['nome']

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome']

class MatriculasViewSet(viewsets.ModelViewSet):
    queryset = Matriculas.objects.all()
    serializer_class = MatriculaSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['estudante__nome', 'data_matricula']
    ordering_fields = ['data_matricula']
