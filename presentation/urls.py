from fastapi import APIRouter
from presentation.controllers.pedidos_controller import router as pedidos_router

main_router = APIRouter()

main_router.include_router(pedidos_router)

__all__ = ['main_router']

