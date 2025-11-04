from rest_framework import serializers
from .models import Categoria, Curso

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
    
    def to_internal_value(self, data):
        try:
            return super().to_internal_value(data)
        except serializers.ValidationError as e:
            # Personalizar mensajes de error en español
            errores = {}
            for field, error_list in e.detail.items():
                if field == 'nombre':
                    errores[field] = 'El nombre es obligatorio y no puede estar vacío'
                elif field == 'descripcion':
                    errores[field] = 'La descripción es obligatoria'
                elif field == 'imagen':
                    errores[field] = 'La imagen debe ser un archivo válido'
                else:
                    errores[field] = error_list
            raise serializers.ValidationError(errores)

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'