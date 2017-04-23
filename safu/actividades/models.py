from django.db import models


class Lugar(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'


class Actividad(models.Model):
    titulo = models.CharField(max_length=32)
    descripcion = models.TextField(blank=False)
    lugar = models.ForeignKey(Lugar)
    fecha = models.DateField(blank=False, null=False)
    imagen = models.ImageField(upload_to='actividades',
                               default='actividades/silueta.png')

    def __str__(self):
        return 'Actividad: {}'.format(self.titulo)

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
