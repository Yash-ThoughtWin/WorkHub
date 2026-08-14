from sqlalchemy.orm import sessionmaker, Session
from app.database.database import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def get_db():
    db = SessionLocal()
    try:
        yield db # gives the API access to db session
    finally:
        db.close() # ensures the session is closed after the request
        
 #"get_db() is a FastAPI dependency that creates a SQLAlchemy session for a request and closes it afterward using a finally block, preventing database connections from remaining open."
