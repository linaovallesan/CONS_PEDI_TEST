from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from CONS_PEDI_TEST.infrastructure.sql_alchemy.mappings import Base

class SessionFactory:
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )
        Base.metadata.create_all(bind=self.engine)
    
    def get_session(self):
        return self.SessionLocal()
