from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente

# Página de inicio
def inicio_live_side(request):
    return render(request, 'inicio.html')

# Agregar paciente
def agregar_paciente(request):
    if request.method == 'POST':
        Paciente.objects.create(
            nom_pac=request.POST.get('nom_pac'),
            ape_pac=request.POST.get('ape_pac'),
            edad_pac=request.POST.get('edad_pac'),
            genero_pac=request.POST.get('genero_pac'),
            tel_pac=request.POST.get('tel_pac'),
            correo_pac=request.POST.get('correo_pac'),
            direccion_pac=request.POST.get('direccion_pac')
        )
        return redirect('ver_pacientes')
    return render(request, 'pacientes/agregar_paciente.html')

# Ver pacientes
def ver_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/ver_pacientes.html', {'pacientes': pacientes})

# Actualizar paciente (mostrar formulario)
def actualizar_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    return render(request, 'pacientes/actualizar_paciente.html', {'paciente': paciente})

# Realizar actualización
def realizar_actualizacion_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    if request.method == 'POST':
        paciente.nom_pac = request.POST.get('nom_pac')
        paciente.ape_pac = request.POST.get('ape_pac')
        paciente.edad_pac = request.POST.get('edad_pac')
        paciente.genero_pac = request.POST.get('genero_pac')
        paciente.tel_pac = request.POST.get('tel_pac')
        paciente.correo_pac = request.POST.get('correo_pac')
        paciente.direccion_pac = request.POST.get('direccion_pac')
        paciente.save()
        return redirect('ver_pacientes')
    return redirect('ver_pacientes')

# Borrar paciente
def borrar_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('ver_pacientes')
    return render(request, 'pacientes/borrar_paciente.html', {'paciente': paciente})
