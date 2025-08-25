# API de Pedidos - Arquitectura Hexagonal

## Estructura del Proyecto
project/
├── application/
│   ├── DTOs/
│   │   └── pedidos_dto.py
│   └── Services/
│       └── pedidos_service.py
├── domain/
│   ├── models/
│   │   └── pedidos.py
│   └── repositories/
│       └── pedidos_repository.py
├── infrastructure/
│   ├── repositories/
│   │   └── pedidos_repository.py
│   ├── sql_alchemy/
│   │   ├── mappings.py
│   │   └── session_factory.py
│   └── unit_of_work.py
├── main.py
├── requirements.txt
└── README.md

## Instalación
1. Crear entorno virtual: `python -m venv venv`
2. Activar entorno: `source venv/bin/activate` (Linux/Mac) o `venv\Scripts\activate` (Windows)
3. Instalar dependencias: `pip install -r requirements.txt`
4. Configurar variable DATABASE_URL en main.py con conexión PostgreSQL
5. Ejecutar: `uvicorn main:app --reload`

## Uso
Endpoint: POST /pedidos/actualizar
Body: {"id_pedido": "12345"}

## Testing
Ejecutar tests: `pytest`