# Configuración de la aplicación de presentación
from fastapi import FastAPI
from presentation.urls import api_router

def create_app() -> FastAPI:
    """
    Factory function para crear la aplicación FastAPI
    
    Returns:
        FastAPI: Instancia configurada de la aplicación
    """
    app = FastAPI(
        title="Sistema de Pedidos - Presentation Layer",
        description="API REST para gestión de pedidos usando arquitectura hexagonal",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )
    
    # Incluir todas las rutas definidas
    app.include_router(api_router)
    
    return app

# Instancia de la aplicación para ser importada
app = create_app()

