# Controlador para manejar las peticiones HTTP relacionadas con pedidos
# Implementa el endpoint GET /cons_pedi/ para actualizar pedidos
from fastapi import APIRouter, HTTPException, Depends
from application.DTOs.pedidos_dto import PedidoInputDTO, PedidoOutputDTO
from application.Services.pedidos_service import PedidosService
from infrastructure.sql_alchemy.session_factory import SessionFactory
from infrastructure.unit_of_work import SQLAlchemyUnitOfWork
from infrastructure.repositories.pedidos_repository import SQLAlchemyPedidosRepository

router = APIRouter()

# Configuración de la base de datos (debe venir de configuración del proyecto)
DATABASE_URL = "postgresql://user:password@localhost/dbname"
session_factory = SessionFactory(DATABASE_URL)

async def get_pedidos_service():
    """
    Dependency injection para obtener el servicio de pedidos
    Crea una nueva sesión y unidad de trabajo para cada request
    """
    session = session_factory.get_session()
    repository = SQLAlchemyPedidosRepository(session)
    uow = SQLAlchemyUnitOfWork(session_factory)
    return PedidosService(repository, uow)

@router.get("/cons_pedi/", response_model=PedidoOutputDTO)
async def actualiza_pedidos(
    id_pedido: str,
    service: PedidosService = Depends(get_pedidos_service)
):
    """
    Endpoint GET para actualizar pedidos
    Recibe el id_pedido como query parameter y retorna el estado de la operación
    
    Args:
        id_pedido (str): ID del pedido a actualizar
        service (PedidosService): Servicio inyectado por dependencia
        
    Returns:
        PedidoOutputDTO: DTO con el estado de la operación
        
    Raises:
        HTTPException 400: Error en la solicitud o pedido no encontrado
        HTTPException 500: Error interno del servidor
    """
    try:
        # Crear DTO de entrada desde el query parameter
        input_dto = PedidoInputDTO(id_pedido=id_pedido)
        
        # Ejecutar el servicio de forma asíncrona
        result = await service.actualizar_pedido(input_dto)  # Se modificó método para coherencia con descripción funcional
        return result
        
    except ValueError as e:
        # Error de validación o pedido no encontrado
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Error interno del servidor
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

