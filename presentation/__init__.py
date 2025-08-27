# Package initialization para la capa de presentación
"""
Módulo de presentación para la aplicación de pedidos
Contiene controladores, URLs y configuración de la aplicación FastAPI
"""

__version__ = "1.0.0"
__all__ = ["app", "api_router"]

# Importaciones para facilitar el acceso
from presentation.apps import app
from presentation.urls import api_router
