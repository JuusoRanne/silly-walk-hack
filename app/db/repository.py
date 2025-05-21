"""
Data access layer for CRUD operations.

This module provides an abstraction layer for database operations,
hiding the implementation details from the service layer.
"""
from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.application import Application
from app.models.schemas import ApplicationCreate, ApplicationUpdate
from sqlalchemy import text
import logging

# Set up logging
logger = logging.getLogger(__name__)

class ApplicationRepository:
    """
    Repository for Application entity CRUD operations.
    """

    @staticmethod
    def create(db: Session, application: Application) -> Application:
        """
        Create a new application in the database.

        Args:
            db (Session): Database session
            application (Application): Application model instance

        Returns:
            Application: Created application with generated ID

        Raises:
            SQLAlchemyError: If database operation fails
        """
        try:
            db.add(application)
            db.commit()
            db.refresh(application)
            return application
        except SQLAlchemyError as e:
            db.rollback()
            logger.error(f"Error creating application: {str(e)}")
            raise

    @staticmethod
    def get_by_id(db: Session, application_id: UUID) -> Optional[Application]:
        """
        Get an application by its ID.

        Args:
            db (Session): Database session
            application_id (UUID): Application UUID

        Returns:
            Optional[Application]: Application if found, None otherwise
        """
        return db.query(Application).filter(Application.id == application_id).first()

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Application]:
        """
        Get a list of applications with pagination.

        Args:
            db (Session): Database session
            skip (int): Number of records to skip
            limit (int): Maximum number of records to return

        Returns:
            List[Application]: List of applications
        """
        return db.query(Application).offset(skip).limit(limit).all()

    @staticmethod
    def update(db: Session, application: Application, updated_data: ApplicationUpdate) -> Application:
        """
        Update an application.

        Args:
            db (Session): Database session
            application (Application): Existing application
            updated_data (ApplicationUpdate): Updated data

        Returns:
            Application: Updated application

        Raises:
            SQLAlchemyError: If database operation fails
        """
        try:
            for key, value in updated_data.dict(exclude_unset=True).items():
                setattr(application, key, value)

            db.commit()
            db.refresh(application)
            return application
        except SQLAlchemyError as e:
            db.rollback()
            logger.error(f"Error updating application: {str(e)}")
            raise

    @staticmethod
    def delete(db: Session, application: Application) -> bool:
        """
        Delete an application.

        Args:
            db (Session): Database session
            application (Application): Application to delete

        Returns:
            bool: True if deleted successfully

        Raises:
            SQLAlchemyError: If database operation fails
        """
        try:
            db.delete(application)
            db.commit()
            return True
        except SQLAlchemyError as e:
            db.rollback()
            logger.error(f"Error deleting application: {str(e)}")
            raise

    @staticmethod
    def is_walk_name_unique(db: Session, walk_name: str, exclude_id: Optional[UUID] = None) -> bool:
        """
        Check if a walk name is unique among all applications.

        Args:
            db (Session): Database session
            walk_name (str): Walk name to check
            exclude_id (Optional[UUID]): Optional ID to exclude from the check

        Returns:
            bool: True if the walk name is unique, False otherwise
        """
        query = db.query(Application).filter(Application.walk_name == walk_name)

        if exclude_id:
            query = query.filter(Application.id != exclude_id)

        return query.first() is None
