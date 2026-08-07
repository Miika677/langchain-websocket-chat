from typing import Generator

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///app.db")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base

def start_session() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class MyTable(Base):
    __tablename__ = "TBD"
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, unique=True, nullable=False)