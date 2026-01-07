"""
SQLAlchemy initialization.
"""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set.")

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
query_count = 0


def get_db():
    """
    FastAPI dependency that provides a database session per request.

    Automatically handles session cleanup.

    Yields:
        Session: Database session for the request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@event.listens_for(Engine, "before_cursor_execute")
def count_queries(conn, cursor, statement, parameters, context, executemany):
    """Event listener that counts database queries for performance monitoring."""
    global query_count
    query_count += 1


def reset_query_count() -> None:
    """Reset the query counter to zero."""
    global query_count
    query_count = 0


def get_query_count() -> int:
    """
    Get the current query count.

    Returns:
        int: Number of queries executed since last reset.
    """
    return query_count


