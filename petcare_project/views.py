from django.http import JsonResponse

"""
Controladores globales para interceptar errores de navegación y servidor
devolviendo un formato JSON estructurado
"""
def custom_404(request, exception):
    return JsonResponse({
        'error': '404 - Ruta no encontrada',
        'detalle': 'El endpoint o recurso solicitado no existe en el sistema PetCare.'
    }, status=404)

def custom_500(request):
    return JsonResponse({
        'error': '500 - Error interno del servidor',
        'detalle': 'El servidor ha encontrado una falla crítica procesando la solicitud.'
    }, status=500)