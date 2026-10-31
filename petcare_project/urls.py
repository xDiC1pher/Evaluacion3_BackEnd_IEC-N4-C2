from django.contrib import admin
from django.urls import path, include
from clinic.views import panel_medico

"""
Configuración de rutas globales del proyecto
Integra los interceptores, la API REST y la interfaz de usuario
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('clinic.urls')),
    path('', panel_medico, name='panel_medico'),
]

""" 
Registro de interceptores globales de errores 
"""
handler404 = 'petcare_project.views.custom_404'
handler500 = 'petcare_project.views.custom_500'