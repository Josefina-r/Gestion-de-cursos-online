from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, CursoViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'cursos', CursoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]