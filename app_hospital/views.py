from django.shortcuts import render, get_object_or_404
from .models import medico,paciente
from .formularios import add_medic as fm
from .formularios import add_pacient as fm1
from django.http import HttpResponseRedirect

def index(request):
    return render(request, "index.html")

def list_med(request):
    medicos = medico.objects.all()
    return render(request,"lismed.html",{"lismed":medicos})

def add_med(request):
    if request.method == "POST":
        formulario = fm.Add_medic(request.POST)
        if formulario.is_valid():
            nuevoreg = medico()
            nuevoreg.Nombre = formulario.cleaned_data["nombre"]
            nuevoreg.Apellido = formulario.cleaned_data["apellido"]
            nuevoreg.Especialidad = formulario.cleaned_data["especialidad"]
            nuevoreg.save()
            return HttpResponseRedirect("/")
    else:
        formulario = fm.Add_medic()

    return render(request, "Add_medic.html", {"form": formulario})

def indexP(request):
    return render(request, "indexP.html")

def list_pacient(request):
    pacientes = paciente.objects.all()
    return render(request,"lispacient.html",{"lispacient":pacientes})

def add_pacient(request):
    if request.method == "POST":
        formulario2 = fm1.Add_pacient(request.POST)
        if formulario2.is_valid():
            nuevopac = paciente()
            nuevopac.Nombre = formulario2.cleaned_data["nombre"]
            nuevopac.Apellido = formulario2.cleaned_data["apellido"]
            nuevopac.Fecha_Nacimiento = formulario2.cleaned_data["fecha_nacimiento"]
            nuevopac.Sexo = formulario2.cleaned_data["sexo"]
            nuevopac.Altura = formulario2.cleaned_data["altura"]
            medico_id = formulario2.cleaned_data["medico_id"]
            nuevopac.Medico_ID = get_object_or_404(medico, ID_Medico=medico_id) # Para la ingresar el valor de la llave primaria,
            nuevopac.save()
            return HttpResponseRedirect("/")
    else:
        formulario2 = fm1.Add_pacient()
    return render(request, "Add_pacient.html", {"form": formulario2})
