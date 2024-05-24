from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
import os

if os.getenv("CONNECTION_STRING"):
    SQLALCHEMY_DATABASE_URL = os.getenv("CONNECTION_STRING")
else:
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:test1234@127.0.0.1:5432/FASTAPIDB"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
metadata = MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


