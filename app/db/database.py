"""
Database connection setup and session management for SQLAlchemy.

This module handles database connection configuration, session management,
and table creation.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from fastapi import Depends

# Load environment variables
load_dotenv()

# Get database URL from environment or use default
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./silly_walks.db")

# Create SQLAlchemy engine
# For SQLite, check_same_thread is needed for use in FastAPI
# For production, use a connection pool with reasonable pool_size, max_overflow, and pool_recycle
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

# Create sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for models
Base = declarative_base()

def get_db():
    """
    Dependency for database session injection.
    Yields a database session and ensures it's closed after use.

    Yields:
        Session: SQLAlchemy database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables():
    """
    Create database tables for all models that inherit from Base.
    Should be called at application startup.
    """
    # Import models here to avoid circular imports
    from app.models.application import Application

    Base.metadata.create_all(bind=engine)
