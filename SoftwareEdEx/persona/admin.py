from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Estudiante, AsistenteExperiencia, Docente


class EstudianteAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellido', 'tipo_identificacion', 'numero_identificacion', 'codigo_uniandes')
	search_fields = ('nombre', 'tipo_identificacion', 'numero_identificacion', 'codigo_uniandes')
	list_filter = ('tipo_identificacion',)


class AsistenteExperienciaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellido', 'tipo_identificacion', 'numero_identificacion', 'codigo_uniandes')
	search_fields = ('nombre', 'tipo_identificacion', 'numero_identificacion', 'codigo_uniandes')
	list_filter = ('tipo_identificacion',)


class DocenteAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'apellido', 'tipo_identificacion', 'numero_identificacion', 'codigo_uniandes')
	search_fields = ('nombre', 'tipo_identificacion', 'numero_identificacion', 'codigo_uniandes')
	list_filter = ('tipo_identificacion',)


admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(AsistenteExperiencia, AsistenteExperienciaAdmin)
admin.site.register(Docente, DocenteAdmin)
