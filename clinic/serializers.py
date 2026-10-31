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
    # Declaramos el campo 'nombre' para que sea calculado por un método interno
    nombre = serializers.SerializerMethodField()

    class Meta:
        model = Veterinario
        fields = '__all__'

    def get_nombre(self, obj):
        nombre_completo = f"{obj.usuario.first_name} {obj.usuario.last_name}".strip()
        
        # Agregamos el prefijo "Dr/a." para mantener coherencia con la UI
        if nombre_completo:
            return f"Dr/a. {nombre_completo}"
        return obj.usuario.username

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