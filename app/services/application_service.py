"""
Application service for handling silly walk grant applications.

This module provides business logic for creating, retrieving, and updating
walk application data while maintaining appropriate separation of concerns.
"""
import logging
from typing import List, Optional
from uuid import UUID
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.schemas import ApplicationCreate, ApplicationUpdate, ApplicationResponse
from app.models.application import Application
from app.db.repository import ApplicationRepository
from app.services.scoring_service import ScoringService

# Set up logging
logger = logging.getLogger(__name__)

class ApplicationService:
    """
    Service for handling business logic related to walk applications.
    """

    @staticmethod
    def create_application(db: Session, application_data: ApplicationCreate) -> ApplicationResponse:
        """
        Create a new walk application with calculated silliness score.

        This method:
        1. Calculates the silliness score
        2. Creates a new Application ORM model
        3. Persists it to the database
        4. Returns a formatted response

        Args:
            db (Session): Database session
            application_data (ApplicationCreate): Validated application data

        Returns:
            ApplicationResponse: Created application with generated ID, score, and timestamp

        Raises:
            ValueError: If validation fails
            Exception: For other unexpected errors
        """
        try:
            # Calculate silliness score
            silliness_score = ScoringService.calculate_score(application_data, db)

            # Create Application ORM model
            new_application = Application(
                applicant_name=application_data.applicant_name,
                walk_name=application_data.walk_name,
                description=application_data.description,
                has_briefcase=application_data.has_briefcase,
                involves_hopping=application_data.involves_hopping,
                number_of_twirls=application_data.number_of_twirls,
                silliness_score=silliness_score,
                status="PendingReview",
                submission_timestamp=datetime.utcnow()
            )

            # Save to database
            created_application = ApplicationRepository.create(db, new_application)

            # Log successful creation (without sensitive data)
            logger.info(f"New application created with ID: {created_application.id}")

            # Return formatted response using Pydantic model
            return ApplicationResponse.from_orm(created_application)

        except ValueError as ve:
            logger.warning(f"Validation error when creating application: {str(ve)}")
            raise
        except Exception as e:
            logger.error(f"Error creating application: {str(e)}")
            raise

    @staticmethod
    def get_application_by_id(db: Session, application_id: UUID) -> Optional[ApplicationResponse]:
        """
        Retrieve an application by its ID.

        Args:
            db (Session): Database session
            application_id (UUID): Application UUID

        Returns:
            Optional[ApplicationResponse]: Application if found, None otherwise

        Raises:
            Exception: For unexpected errors
        """
        try:
            application = ApplicationRepository.get_by_id(db, application_id)
            if application:
                return ApplicationResponse.from_orm(application)
            return None
        except Exception as e:
            logger.error(f"Error retrieving application with ID {application_id}: {str(e)}")
            raise

    @staticmethod
    def get_all_applications(db: Session, skip: int = 0, limit: int = 100) -> List[ApplicationResponse]:
        """
        Retrieve a list of applications with pagination.

        Args:
            db (Session): Database session
            skip (int): Number of records to skip
            limit (int): Maximum number of records to return

        Returns:
            List[ApplicationResponse]: List of applications

        Raises:
            Exception: For unexpected errors
        """
        try:
            applications = ApplicationRepository.get_all(db, skip, limit)
            return [ApplicationResponse.from_orm(app) for app in applications]
        except Exception as e:
            logger.error(f"Error retrieving applications: {str(e)}")
            raise
