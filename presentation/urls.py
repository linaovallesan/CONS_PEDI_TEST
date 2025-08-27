# Configuración de URLs para la aplicación de presentación
from fastapi import APIRouter
from presentation.controllers.pedidos_controller import router as pedidos_router

# Router principal que agrupa todos los endpoints
api_router = APIRouter()

# Incluir rutas de pedidos
api_router.include_router(pedidos_router)

# Exportar el router para ser usado en la aplicación principal
__all__ = ["api_router"]

