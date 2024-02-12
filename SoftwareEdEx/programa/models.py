from django.db import models
from datetime import datetime, date

class Programa(models.Model):

    ESTADO_CHOICES = [
        ('PE', 'Pendiente por iniciar'),
        ('EC', 'En curso'),
        ('IN', 'Inactivo'),
        ('EJ', 'Ejecutado'),
        ('OTRO', 'Otro'),
    ]

    UNIDAD_CHOICES = [
        ('PAB', 'Programas Abiertos'),
        ('PCO', 'Programas Corporativos'),
        ('PRO', 'Proyectos'),
        ('MAE', 'Maestria'),
        ('ESP', 'Especializaciones'),
        ('PRE', 'Pregrado'),
    ]

    estado = models.CharField(
        max_length=5,
        choices=ESTADO_CHOICES,
        default='IN'
    )

    unidad = models.CharField(
        max_length=5,
        choices=UNIDAD_CHOICES,
        default='PAB'
    )

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    seccion = models.CharField(max_length=255)
    periodo_academico = models.CharField(max_length=255)
    crn = models.CharField(max_length=255)
    intensidad_horaria_semanal = models.FloatField()
    duracion_total_en_horas = models.FloatField()

    requiere_asistente_de_experiencia = models.BooleanField()
    requiere_asistencia_minima = models.BooleanField()
    requiere_nota_minima = models.BooleanField()

    #TODO: FK ASISTENTE DE EXPERIENCIA
    porcentaje_asistencia_minima = models.DecimalField(decimal_places=2, max_digits=3)
    nota_minima = models.DecimalField(decimal_places=2, max_digits=3)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nombre


class Modulo(models.Model):
    programa = models.ForeignKey(Programa, related_name='modulos', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    orden_modulo = models.PositiveIntegerField()

    class Meta:
        ordering = ['orden_modulo']
        unique_together = ('programa', 'orden_modulo')  # This ensures that the order is unique within a Programa

#TODO: Definir un valor por defecto donde - Una sesion puede ser "trabajo individual" o "trabajo asincronico"
class Sesion(models.Model):
    modulo = models.ForeignKey(Modulo, related_name='sesiones', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    orden_sesion = models.PositiveIntegerField()

    class Meta:
        ordering = ['orden_sesion']
        unique_together = ('modulo', 'orden_sesion')  # This ensures that the order is unique within a Modulo
        verbose_name = "Sesion"
        verbose_name_plural = "Sesiones"




class Clase(models.Model):
    UBICACION_CHOICES = [
        ('VI', 'Virtual'),
        ('PR', 'Presencial'),
    ]
    ubicacion = models.CharField(
        max_length=5,
        choices=UBICACION_CHOICES,
        default='PR'
    )

    sesion = models.ForeignKey(Sesion, related_name='clases', on_delete=models.CASCADE)
    fecha_de_clase = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    orden_clase = models.PositiveIntegerField()  # This field determines the order of classes within a session.
    #TODO: FK PROFESOR

    class Meta:
        ordering = ['orden_clase']
        unique_together = ('sesion', 'orden_clase')  # Ensures unique order within each session

    @property
    def total_horas(self):
        start_time = datetime.combine(datetime.today(), self.hora_inicio)
        end_time = datetime.combine(datetime.today(), self.hora_fin)
        duration_timedelta = end_time - start_time
        duration_in_hours = duration_timedelta.total_seconds() / 3600.0
        return duration_in_hours





