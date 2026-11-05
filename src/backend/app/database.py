from sqlalchemy.orm import Session
from .models import db
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db)


def get_db():
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()
