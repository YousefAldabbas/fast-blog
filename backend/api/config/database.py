import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

SQLALCHEMY_DATABASE_URL = str(os.getenv("SQLALCHEMY_DATABASE_URL"))
engine = create_engine(SQLALCHEMY_DATABASE_URL)



SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()


def get_db():
    """
    It creates a database connection, and then yields it to the caller.

    The caller can then use the connection, and when it's done, the connection is closed.

    The yield keyword is what makes this function a generator.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
