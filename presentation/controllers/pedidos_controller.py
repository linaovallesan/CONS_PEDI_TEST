from fastapi import APIRouter, Depends, HTTPException, status
from application.DTOs.pedidos_dto import PedidoInputDTO, PedidoOutputDTO
from application.Services.pedidos_service import PedidosService
from infrastructure.unit_of_work import SQLAlchemyUnitOfWork
from infrastructure.repositories.pedidos_repository import SQLAlchemyPedidosRepository
from infrastructure.sql_alchemy.session_factory import SessionFactory

DATABASE_URL = "postgresql://user:password@localhost/dbname"
session_factory = SessionFactory(DATABASE_URL)

router = APIRouter(prefix="/cons_pedi", tags=["pedidos"])

async def get_pedidos_service():
    session = session_factory.get_session()
    repository = SQLAlchemyPedidosRepository(session)
    uow = SQLAlchemyUnitOfWork(session_factory)
    return PedidosService(repository, uow)

@router.get("/", response_model=PedidoOutputDTO, status_code=status.HTTP_200_OK)
async def actualiza_pedidos(
    id_pedido: str,
    service: PedidosService = Depends(get_pedidos_service)
):
    try:
        input_dto = PedidoInputDTO(id_pedido=id_pedido)
        result = service.actualizar_pedido_a_cerrado(input_dto)
        return result
    except ValueError as e:
        if "no encontrado" in str(e).lower():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno del servidor: {str(e)}"
        )

