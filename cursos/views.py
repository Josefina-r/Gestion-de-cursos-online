from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Categoria, Curso
from .serializers import CategoriaSerializer, CursoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def create(self, request, *args, **kwargs):
        try:
            if not request.data:
                return Response(
                    {'error': 'No se han enviado datos. Por favor, complete el formulario.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                # Formatear los errores de una manera más amigable
                errores = {}
                for campo, mensajes in serializer.errors.items():
                    if campo == 'nombre':
                        errores[campo] = 'El nombre de la categoría es obligatorio'
                    elif campo == 'descripcion':
                        errores[campo] = 'La descripción de la categoría es obligatoria'
                    elif campo == 'imagen':
                        errores[campo] = 'El formato de la imagen no es válido'
                    else:
                        errores[campo] = mensajes[0] if isinstance(mensajes, list) else str(mensajes)

                return Response(
                    {
                        'error': 'Por favor, corrija los siguientes errores:',
                        'detalles': errores
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {
                    'mensaje': 'Categoría creada exitosamente',
                    'datos': serializer.data
                },
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        except Exception as e:
            return Response(
                {
                    'error': 'Error al crear la categoría',
                    'detalles': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def get_queryset(self):
        queryset = Curso.objects.all()
        categoria_id = self.request.query_params.get('categoria_id')
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)
        return queryset