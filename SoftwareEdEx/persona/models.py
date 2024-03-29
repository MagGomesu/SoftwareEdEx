from django.db import models


# Create your models here.
class Persona(models.Model):
	# Choices for Tipo de Identificación
	TIPO_IDENTIFICACION_CHOICES = [
		('CC', 'Cédula de Ciudadanía'),
		('TI', 'Tarjeta de Identidad'),
		('CE', 'Cédula de Extranjería'),
		('PAS', 'Pasaporte'),
		('OTRO', 'Otro'),
	]

	tipo_identificacion = models.CharField(
		max_length=5,
		choices=TIPO_IDENTIFICACION_CHOICES,
		default='CC'  # Default to Cédula de Ciudadanía
	)

	# Auto-generated primary key
	id = models.AutoField(primary_key=True)

	numero_identificacion = models.CharField(max_length=20)
	codigo_uniandes = models.PositiveIntegerField()
	genero = models.CharField(max_length=1)
	nombre = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255)
	profesion = models.CharField(max_length=255)
	cargo = models.CharField(max_length=255)
	nacionalidad = models.CharField(max_length=255)
	direccion = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	celular = models.CharField(max_length=20)

	def __str__(self):
		return f"{self.nombre} {self.apellido}"

	class Meta:
		abstract = True


class Estudiante(Persona):
	estado = models.CharField(max_length=50)


class Docente(Persona):
	area = models.CharField(max_length=100)
	tipo_contrato = models.CharField(max_length=100)
	tarifa_hora = models.IntegerField()

class AsistenteExperiencia(Persona):
	programa_academico_que_cursa = models.CharField(max_length=100)

	class Meta:
		verbose_name = "Asistente de experiencia"
		verbose_name_plural = "Asistentes de experiencia"