from django.contrib import admin
from .models import Tutor, Mascota, Veterinario, Cita, FichaClinica, Recordatorio

"""
Configuración administrativa para la entidad Tutor
Habilita búsqueda por nombre, apellido y email
"""
@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'email')
    search_fields = ('nombre', 'apellido', 'email')

"""
Configuración administrativa para la entidad Mascota
Filtra por especie e integra búsqueda por nombre y tutor
"""
@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'tutor')
    list_filter = ('especie',)
    search_fields = ('nombre', 'tutor__nombre', 'tutor__apellido')

"""
Configuración administrativa para la entidad Veterinario
"""
@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'especialidad', 'telefono')
    search_fields = ('usuario__first_name', 'usuario__last_name', 'especialidad')

"""
Configuración administrativa para la entidad Cita
Permite filtrar por estado y fecha, optimizando la gestión de disponibilidad
"""
@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'veterinario', 'fecha_hora', 'estado')
    list_filter = ('estado', 'fecha_hora', 'veterinario')
    search_fields = ('mascota__nombre', 'motivo')

"""
Configuración administrativa para la entidad FichaClinica
"""
@admin.register(FichaClinica)
class FichaClinicaAdmin(admin.ModelAdmin):
    list_display = ('cita', 'fecha_creacion')
    search_fields = ('cita__mascota__nombre', 'diagnostico')

"""
Configuración administrativa para la entidad Recordatorio
Facilita el seguimiento de vacunas y controles completados o pendientes
"""
@admin.register(Recordatorio)
class RecordatorioAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'mascota', 'fecha_programada', 'completado')
    list_filter = ('tipo', 'completado', 'fecha_programada')
    search_fields = ('mascota__nombre', 'descripcion')