# Configuración de URLs para la aplicación de presentación
# Define los endpoints y sus controladores correspondientes
from fastapi import APIRouter
from presentation.controllers.pedidos_controller import router as pedidos_router

# Router principal que agrupa todos los endpoints
main_router = APIRouter()

# Incluir el router de pedidos con el prefijo correspondiente
main_router.include_router(pedidos_router, prefix="/pedidos", tags=["pedidos"])

# Exportar el router principal para ser usado en la aplicación FastAPI
router = main_router

