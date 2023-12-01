from django.shortcuts import render
from .models import Estudiante

def dashboard_view(request):
    # Query the database for all Participante instances
    estudiantes = Estudiante.objects.all()

    # Pass the participantes list to the template via the context dictionary
    context = {
        'active_item': 'dashboard',
        'estudiantes': estudiantes  # Add this line to include the personas in the context
    }
    return render(request, 'persona/persona_list.html', context)

def edit_estudiante_view(request, id):
    # Logic to handle editing an Estudiante
    pass

def delete_estudiante_view(request, id):
    # Logic to handle editing an Estudiante
    pass