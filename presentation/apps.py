# Configuración de la aplicación de presentación para Django
# Define la aplicación y sus configuraciones específicas
from django.apps import AppConfig

class PresentationConfig(AppConfig):
    """
    Configuración de la aplicación de presentación
    Esta aplicación maneja los controladores y endpoints de la API
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'presentation'
    verbose_name = 'Capa de Presentación'
    
    def ready(self):
        """
        Método ejecutado cuando la aplicación está lista
        Se puede usar para inicializar configuraciones o servicios
        """
        # Importar aquí para evitar importaciones circulares
        pass
