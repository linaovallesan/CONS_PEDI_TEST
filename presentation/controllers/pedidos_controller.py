from fastapi import APIRouter, HTTPException, Depends
from application.DTOs.pedidos_dto import PedidoInputDTO, PedidoOutputDTO
from application.services.pedidos_service import PedidosService
from infrastructure.sql_alchemy.session_factory import SessionFactory
from infrastructure.unit_of_work import SQLAlchemyUnitOfWork
from infrastructure.repositories.pedidos_repository import SQLAlchemyPedidosRepository


router = APIRouter(prefix="/post_test", tags=["pedidos"])

DATABASE_URL = "postgresql://user:password@localhost/dbname"
session_factory = SessionFactory(DATABASE_URL)


async def get_pedidos_service():
    session = session_factory.get_session()
    repository = SQLAlchemyPedidosRepository(session)
    uow = SQLAlchemyUnitOfWork(session_factory)
    return PedidosService(repository, uow)


@router.post("", response_model=PedidoOutputDTO, status_code=200)
async def actualiza_pedidos(
    input_dto: PedidoInputDTO,
    service: PedidosService = Depends(get_pedidos_service)
):
    try:
        result = await service.actualizar_pedido_a_cerrado(input_dto)
        return result
        
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error interno al procesar la solicitud: {str(e)}"
        )


