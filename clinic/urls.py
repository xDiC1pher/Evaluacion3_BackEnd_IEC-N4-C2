from django.urls import path, include
from rest_framework import routers
from .views import (TutorViewSet, MascotaViewSet, VeterinarioViewSet,
                    CitaViewSet, FichaClinicaViewSet, RecordatorioViewSet)

"""
Enrutador principal de la API REST para el módulo clinic
"""
router = routers.DefaultRouter()
router.register(r'tutores', TutorViewSet)
router.register(r'mascotas', MascotaViewSet)
router.register(r'veterinarios', VeterinarioViewSet)
router.register(r'citas', CitaViewSet)
router.register(r'fichas', FichaClinicaViewSet)
router.register(r'recordatorios', RecordatorioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]