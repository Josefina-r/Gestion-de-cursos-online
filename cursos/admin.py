from django.contrib import admin

from django.contrib import admin
from .models import Categoria, Curso

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'fecha_creacion']
    search_fields = ['nombre']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'duracion', 'precio', 'instructor', 'categoria', 'fecha_creacion']
    list_filter = ['categoria', 'fecha_creacion']
    search_fields = ['nombre', 'instructor']