# Controlador para manejar las operaciones de pedidos
from fastapi import APIRouter, Depends, HTTPException, status
from application.DTOs.pedidos_dto import PedidoInputDTO, PedidoOutputDTO
from application.services.pedidos_service import PedidosService
from infrastructure.unit_of_work import SQLAlchemyUnitOfWork
from infrastructure.repositories.pedidos_repository import SQLAlchemyPedidosRepository
from infrastructure.sql_alchemy.session_factory import SessionFactory

# Configuración de la base de datos (debería venir de configuración)
DATABASE_URL = "postgresql://user:password@localhost/dbname"
session_factory = SessionFactory(DATABASE_URL)

# Crear router para los endpoints de pedidos
router = APIRouter(prefix="/post_test", tags=["pedidos"])

async def get_pedidos_service():
    """
    Dependency injection para el servicio de pedidos
    Crea una nueva sesión y unidad de trabajo para cada request
    """
    session = session_factory.get_session()
    repository = SQLAlchemyPedidosRepository(session)
    uow = SQLAlchemyUnitOfWork(session_factory)
    return PedidosService(repository, uow)

@router.post(
    "",
    response_model=PedidoOutputDTO,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Pedido actualizado exitosamente"},
        400: {"description": "Error por datos inválidos"},
        404: {"description": "Pedido no encontrado"},
        500: {"description": "Error interno del servidor"}
    }
)
async def actualiza_pedidos(
    input_dto: PedidoInputDTO,
    service: PedidosService = Depends(get_pedidos_service)
) -> PedidoOutputDTO:
    """
    Endpoint para actualizar pedidos mediante método POST
    
    Args:
        input_dto: DTO con el ID del pedido a actualizar
        service: Servicio inyectado para procesar la lógica de negocio
    
    Returns:
        PedidoOutputDTO: Estado de la operación
        
    Raises:
        HTTPException: 400 para errores de validación, 404 si no encuentra el pedido
    """
    try:
        result = await service.actualizar_pedido(input_dto)
        return result
    except ValueError as e:
        # Manejar errores de validación (ID inválido o pedido no encontrado)
        if "no encontrado" in str(e):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        # Manejar errores inesperados
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno del servidor: {str(e)}"
        )

