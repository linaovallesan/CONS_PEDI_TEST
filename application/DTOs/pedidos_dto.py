from pydantic import BaseModel, Field
from typing import Optional

class PedidoInputDTO(BaseModel):
    id_pedido: str = Field(..., description="ID del pedido a actualizar")
    
    class Config:
        schema_extra = {
            "example": {
                "id_pedido": "12345"
            }
        }

class PedidoOutputDTO(BaseModel):
    status: str = Field(..., description="Estado de la operación")
    
    class Config:
        schema_extra = {
            "example": {
                "status": "pedido 12345 actualizado"
            }
        }
