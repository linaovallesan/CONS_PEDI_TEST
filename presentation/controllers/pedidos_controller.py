from fastapi import APIRouter, Depends, HTTPException
from application.DTOs.pedidos_dto import PedidoInputDTO, PedidoOutputDTO
from application.Services.pedidos_service import PedidosService
from infrastructure.sql_alchemy.session_factory import SessionFactory
from infrastructure.unit_of_work import SQLAlchemyUnitOfWork
from infrastructure.repositories.pedidos_repository import SQLAlchemyPedidosRepository

router = APIRouter(prefix="/test", tags=["pedidos"])

DATABASE_URL = "postgresql://user:password@localhost/dbname"
session_factory = SessionFactory(DATABASE_URL)

async def get_pedidos_service():
    session = session_factory.get_session()
    repository = SQLAlchemyPedidosRepository(session)
    uow = SQLAlchemyUnitOfWork(session_factory)
    return PedidosService(repository, uow)

@router.get("", response_model=PedidoOutputDTO)
async def actualiza_pedidos(
    id_pedido: str,
    service: PedidosService = Depends(get_pedidos_service)
):
    try:
        input_dto = PedidoInputDTO(id_pedido=id_pedido)
        result = service.actualizar_pedido(input_dto)  # Assuming 'actualizar_pedido' correctly represents the method to update an order (and not specifically 'close' an order as initially named) 
        
        return result
        
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

