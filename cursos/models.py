from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='categorias/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categorias'

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    duracion = models.IntegerField(help_text="Duración en horas")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    instructor = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='cursos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'cursos'