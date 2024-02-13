from django.contrib.admin.sites import site
from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction
from django.http import (
    HttpResponseRedirect,
    HttpResponse
)
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.urls import reverse
from .forms import (
    ProgramaFilterForm,
    SesionForm,
    ProgramaForm,
    ModuloForm
)
from .models import (
    Programa,
    Sesion,
    Modulo,
    Clase
)

def edit_sesion(request, pk):
    item = get_object_or_404(Sesion, pk=pk)
    form = SesionForm(instance=item)
    context = {
        'form': form,
        'sesion_id': pk,
    }
    return render(request, 'programa/edit_sesion_modal.html', context)

def edit_modulo(request, pk):
    item = get_object_or_404(Modulo, pk=pk)
    form = ModuloForm(instance=item)
    context = {
        'form': form,
        'modulo_id': pk,
    }
    return render(request, 'programa/edit_modulo_modal.html', context)



def save_programa(request):
    if request.method == 'POST':
        deleted_clases_ids = request.POST.get('deletedClases', '')

        # Start a database transaction
        with transaction.atomic():
            if deleted_clases_ids:
                # Convert the string of IDs into a list of integers
                deleted_ids_list = [int(id) for id in deleted_clases_ids.split(',') if id.isdigit()]

                # Delete the Clases by ID
                Clase.objects.filter(id__in=deleted_ids_list).delete()

                # Here you would include any additional logic for saving/updating other parts
                # of your form related to Programa, Modulo, Sesion, etc.
                # For example, updating a Programa's description might look like this:
                # programa_id = request.POST.get('programa_id')
                # description = request.POST.get('descripcion', '')
                # Programa.objects.filter(id=programa_id).update(descripcion=description)

            # Commit the transaction
            # Note: If an exception is raised within the with-block, the transaction will be rolled back.

        # Redirect to a new URL: This is a placeholder redirect, adjust to your needs
        return redirect('your_success_url')
    else:
        # If not a POST request, just return to the main page or form
        return HttpResponse("Invalid request", status=400)


@staff_member_required
def edit_programa(request, pk):
    programa = get_object_or_404(Programa, pk=pk)

    if request.method == 'POST':
        # Initialize the form with instance data and the POST data
        form = ProgramaForm(request.POST, request.FILES, instance=programa)
        if form.is_valid():
            # Save the form, thus updating the instance
            form.save()
            # Redirect, for example, to the view of the updated Programa
            return HttpResponseRedirect(reverse('view_programa'))
    else:
        # Initialize the form with instance data for editing
        form = ProgramaForm(instance=programa)

    context = {
        **site.each_context(request),
        'site_title': 'Editar Programa',
        'programa' : programa,
        'form': form,
    }
    return render(request, 'programa/edit_programa.html', context)


@staff_member_required
def add_programa(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a new URL, for example, the list of Programas
            return HttpResponseRedirect(reverse('view_programa'))
    else:
        form = ProgramaForm()

    context = {
        **site.each_context(request),
        'site_title': 'Añadir Programa',
        'form': form,
    }
    return render(request, 'programa/add_programa.html', context)



def view_programa(request):
    form = ProgramaFilterForm(request.GET)
    filters_applied = any(value for key, value in request.GET.items() if key != 'page')
    programas = Programa.objects.all()

    if form.is_valid():
        if form.cleaned_data['estado']:
            programas = programas.filter(estado=form.cleaned_data['estado'])
        if form.cleaned_data['unidad']:
            programas = programas.filter(unidad=form.cleaned_data['unidad'])
        if form.cleaned_data['crn']:
            programas = programas.filter(crn=form.cleaned_data['crn'])
        if form.cleaned_data['fecha_inicio']:
            programas = programas.filter(fecha_inicio__gte=form.cleaned_data['fecha_inicio'])
        if form.cleaned_data['fecha_fin']:
            programas = programas.filter(fecha_fin__lte=form.cleaned_data['fecha_fin'])

    results_count = programas.count()

    context = {
        **site.each_context(request),
        'site_title': 'Programas',
        'form': form,
        'programas': programas,
        'filters_applied': filters_applied,
        'results_count': results_count,
    }
    return render(request, 'programa/view_programa.html', context)