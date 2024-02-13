from django import forms
from .models import Programa, Modulo, Sesion


class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = '__all__'

class ProgramaFilterForm(forms.Form):
    crn = forms.CharField(widget=forms.TextInput, required=False, label='CRN')
    estado = forms.ChoiceField(choices=Programa.ESTADO_CHOICES, required=False, label='Estado')
    unidad = forms.ChoiceField(choices=Programa.UNIDAD_CHOICES, required=False, label='Unidad')
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False, label='Fecha Inicio')
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False, label='Fecha Fin')


class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['nombre']

class SesionForm(forms.ModelForm):
    class Meta:
        model = Sesion
        fields = '__all__'
        exclude = ['modulo', 'orden_sesion']
