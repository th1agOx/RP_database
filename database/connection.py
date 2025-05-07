from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database.models import Base

DATABASE_URL = 'sqlite:///C:/banco_read_pdf/database/rpdatabase.db'

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

def get_session():
    return SessionLocal()