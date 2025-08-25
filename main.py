from fastapi import FastAPI, HTTPException, Depends
from CONS_PEDI_TEST.infrastructure.sql_alchemy.session_factory import SessionFactory
from CONS_PEDI_TEST.infrastructure.unit_of_work import SQLAlchemyUnitOfWork
from CONS_PEDI_TEST.infrastructure.repositories.pedidos_repository import SQLAlchemyPedidosRepository
from CONS_PEDI_TEST.application.Services.pedidos_service import PedidosService
from CONS_PEDI_TEST.application.DTOs.pedidos_dto import PedidoInputDTO, PedidoOutputDTO


app = FastAPI(title="API de Pedidos", description="API para consultar y actualizar pedidos")

# Configuración de la base de datos
DATABASE_URL = "postgresql://user:password@localhost/dbname"
session_factory = SessionFactory(DATABASE_URL)


def get_pedidos_service():
    session = session_factory.get_session()
    repository = SQLAlchemyPedidosRepository(session)
    uow = SQLAlchemyUnitOfWork(session_factory)
    return PedidosService(repository, uow)


@app.post("/pedidos/actualizar", response_model=PedidoOutputDTO)
def actualizar_pedido(
    input_dto: PedidoInputDTO,
    service: PedidosService = Depends(get_pedidos_service)
):
    try:
        return service.actualizar_pedido_a_cerrado(input_dto)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
def health_check():
    return {"status": "healthy"}
