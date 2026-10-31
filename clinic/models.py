from django.db import models
from django.contrib.auth.models import User

"""
Modelo representativo de los tutores o dueños de las mascotas para operaciones CRUD
"""
class Tutor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

"""
Modelo representativo de las mascotas pacientes de la clínica
"""
class Mascota(models.Model):
    ESPECIE_CHOICES = [
        ('Canino', 'Canino'),
        ('Felino', 'Felino'),
        ('Exotico', 'Exótico'),
    ]
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='mascotas')
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50, choices=ESPECIE_CHOICES)
    raza = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - Tutor: {self.tutor.apellido}"

"""
Modelo para gestionar la disponibilidad y agendamiento por profesional veterinario
"""
class Veterinario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"Dr/Dra. {self.usuario.last_name} - {self.especialidad}"

"""
Modelo para el agendamiento de citas médicas y prevención de solapamientos
"""
class Cita(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Realizada', 'Realizada'),
        ('Cancelada', 'Cancelada'),
    ]
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='citas')
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, related_name='citas')
    fecha_hora = models.DateTimeField()
    motivo = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')

    def __str__(self):
        return f"Cita: {self.mascota.nombre} con {self.veterinario} - {self.fecha_hora}"

"""
Modelo de la Ficha Clínica Digital integrando diagnósticos, tratamientos, recetas y exámenes
"""
class FichaClinica(models.Model):
    cita = models.OneToOneField(Cita, on_delete=models.CASCADE, related_name='ficha')
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    receta = models.TextField(blank=True, null=True)
    examenes = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ficha de {self.cita.mascota.nombre} - {self.fecha_creacion.date()}"

"""
Módulo de recordatorios automatizados para vacunación y controles periódicos
"""
class Recordatorio(models.Model):
    TIPO_CHOICES = [
        ('Vacuna', 'Vacunación'),
        ('Control', 'Control Periódico'),
    ]
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='recordatorios')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descripcion = models.CharField(max_length=200)
    fecha_programada = models.DateField()
    completado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.tipo} para {self.mascota.nombre} - {self.fecha_programada}"