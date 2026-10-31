from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Tutor, Mascota, Veterinario, Cita, FichaClinica, Recordatorio
from .serializers import (TutorSerializer, MascotaSerializer, VeterinarioSerializer,
                          CitaSerializer, FichaClinicaSerializer, RecordatorioSerializer)

"""
ViewSets para la gestión CRUD completa de las entidades del sistema PetCare
"""
class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class FichaClinicaViewSet(viewsets.ModelViewSet):
    queryset = FichaClinica.objects.all()
    serializer_class = FichaClinicaSerializer

class RecordatorioViewSet(viewsets.ModelViewSet):
    queryset = Recordatorio.objects.all()
    serializer_class = RecordatorioSerializer

"""
Vista principal del Panel Médico.
Requiere autenticación de usuario para garantizar la seguridad del sistema.
Recupera y expone las citas pendientes y los recordatorios activos del caso PetCare.
"""
@login_required(login_url='/admin/login/')
def panel_medico(request):
    citas = Cita.objects.all().order_by('fecha_hora')
    recordatorios = Recordatorio.objects.filter(completado=False).order_by('fecha_programada')
    
    context = {
        'citas': citas,
        'recordatorios': recordatorios
    }
    return render(request, 'panel.html', context)