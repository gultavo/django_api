from django.urls import path, include
from rest_framework import routers
from .views import EstudantesViewSet, CursosViewSet, MatriculasViewSet

router = routers.DefaultRouter()
router.register('estudantes', EstudantesViewSet)
router.register('cursos', CursosViewSet)
router.register('matriculas', MatriculasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]