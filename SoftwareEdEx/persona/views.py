from django.shortcuts import render

from django.views.generic import ListView
from .models import Persona
from django.shortcuts import render

def dashboard_view(request):
    # You can pass context variables to the template as needed.
    context = {'active_item': 'dashboard'}  # Example context variable
    return render(request, 'persona/persona_list.html', context)


