from fastapi import FastAPI
from presentation.urls import main_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="API de Pedidos - Arquitectura Hexagonal",
        description="API para gestión de pedidos usando arquitectura hexagonal",
        version="1.0.0"
    )
    
    app.include_router(main_router)
    
    return app


app = create_app()


