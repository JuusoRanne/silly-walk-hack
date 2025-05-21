"""
API routes for silly walk grant applications.

This module defines the HTTP endpoints for the application API.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID

from app.db.database import get_db
from app.auth.api_key_auth import get_api_key
from app.models.schemas import ApplicationCreate, ApplicationResponse
from app.services.application_service import ApplicationService
from app.utils.security import sanitize_log_data

import logging

# Set up logging
logger = logging.getLogger(__name__)

# Create router
router = APIRouter()

@router.post(
    "/applications",
    response_model=ApplicationResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Submit a new silly walk application",
    description="""
    Submit a new application for a silly walk grant.

    This endpoint requires API key authentication via the X-API-Key header.

    The silliness score will be calculated automatically based on:
    - Base score: 10 points if description is longer than 20 characters
    - Briefcase bonus: +5 points if application involves a briefcase
    - Hopping bonus: +3 points for each mention of "hop" or "hopping" in the description (max 15)
    - Twirltastic score: +2 points for each twirl, up to a maximum of 20 points
    - Originality bonus: +7 points if the walk name is unique

    The application status will be set to "PendingReview" initially.
    """,
    responses={
        201: {"description": "Application successfully created"},
        400: {"description": "Invalid input data"},
        401: {"description": "Missing API key"},
        403: {"description": "Invalid API key"},
        500: {"description": "Internal server error"}
    }
)
async def create_application(
    application: ApplicationCreate,
    db: Session = Depends(get_db),
    api_key: str = Depends(get_api_key)  # This dependency handles API key validation
):
    """
    Create a new silly walk grant application.

    Args:
        application (ApplicationCreate): Application data
        db (Session): Database session
        api_key (str): API key for authentication

    Returns:
        ApplicationResponse: Created application with generated ID, score, and status

    Raises:
        HTTPException: For validation errors or server errors
    """
    try:
        # Log sanitized request (no sensitive data)
        sanitized_data = sanitize_log_data(application.dict())
        logger.info(f"Processing application submission: {sanitized_data}")

        # Use application service to handle business logic
        created_application = ApplicationService.create_application(db, application)

        # Return success response with created application
        return created_application

    except ValueError as ve:
        # Handle validation errors
        logger.warning(f"Validation error in application submission: {str(ve)}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ve)
        )
    except Exception as e:
        # Handle unexpected errors
        logger.error(f"Error creating application: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing the application"
        )
