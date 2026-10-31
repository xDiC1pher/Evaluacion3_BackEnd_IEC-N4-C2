from rest_framework import serializers
from .models import Tutor, Mascota, Veterinario, Cita, FichaClinica, Recordatorio

"""
Serializador para la entidad Tutor
"""
class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

"""
Serializador para la entidad Mascota
"""
class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'

"""
Serializador para la entidad Veterinario
"""
class VeterinarioSerializer(serializers.ModelSerializer):
    # Genera un nuevo campo 'nombre' leyendo el apellido del User vinculado. 
    # Puede cambiar 'usuario.last_name' por 'usuario.username' si lo prefiere.
    nombre = serializers.CharField(source='usuario.last_name', read_only=True)

    class Meta:
        model = Veterinario
        fields = '__all__'

"""
Serializador para la entidad Cita
"""
class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'

"""
Serializador para la Ficha Clínica
"""
class FichaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaClinica
        fields = '__all__'

"""
Serializador para Recordatorios
"""
class RecordatorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recordatorio
        fields = '__all__'