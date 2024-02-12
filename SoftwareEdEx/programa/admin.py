from django.contrib import admin

from django.contrib import admin
from .models import Programa, Modulo, Clase, Sesion


class ProgramaAdmin(admin.ModelAdmin):
	list_display = ('crn', 'nombre', 'descripcion', 'periodo_academico', 'unidad', 'seccion', )
	search_fields = ('nombre', 'unidad', 'crn')
	list_filter = ('id', 'crn', 'nombre')

admin.site.register(Programa, ProgramaAdmin)
admin.site.register(Modulo)
admin.site.register(Sesion)
admin.site.register(Clase)
