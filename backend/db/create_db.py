from backend.db import Base, engine, MyTable

Base.metadata.create_all(bind=engine)