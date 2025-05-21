from fastapi import APIRouter, Depends, HTTPException, status, Header, Query
from pydantic import BaseModel, Field, constr
from uuid import uuid4
from typing import Optional, List, Dict, Any
from app.services.application_service import create_application, get_application, get_all_applications
from app.api.dependencies import verify_api_key

router = APIRouter()

class ApplicationSubmissionRequest(BaseModel):
    applicant_name: constr(strip_whitespace=True, min_length=1, max_length=100)
    walk_name: constr(strip_whitespace=True, min_length=1, max_length=100)
    description: constr(strip_whitespace=True, min_length=1, max_length=1000)
    has_briefcase: bool
    involves_hopping: bool
    number_of_twirls: int = Field(..., ge=0, le=100)

class ApplicationSubmissionResponse(BaseModel):
    application_id: str
    silliness_score: int
    status: str

class ApplicationResponse(BaseModel):
    id: str
    applicant_name: str
    walk_name: str
    description: str
    has_briefcase: bool
    involves_hopping: bool
    number_of_twirls: int
    silliness_score: int
    status: str
    submission_timestamp: str

class ApplicationListResponse(BaseModel):
    applications: List[Dict[str, Any]]
    total: int

@router.post(
    "/applications",
    response_model=ApplicationSubmissionResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Submit a new silly walk grant application",
    description="Accepts a new silly walk grant application, validates input, calculates silliness score, persists the application, and returns the application ID and score.",
    tags=["Applications"],
    responses={
        201: {"description": "Application submitted successfully"},
        400: {"description": "Invalid application data"},
        401: {"description": "Missing API key"},
        403: {"description": "Invalid API key"},
        500: {"description": "Internal server error"}
    }
)
def submit_application(
    application: ApplicationSubmissionRequest,
    api_key: str = Depends(verify_api_key)
):
    """
    Submit a new silly walk grant application.
    
    The application data is validated, a silliness score is calculated,
    and the application is stored in the system.
    """
    try:
        result = create_application(application.dict())
        return result
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid application data."
        ) from exc
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )

@router.get(
    "/applications/{application_id}",
    response_model=ApplicationResponse,
    status_code=status.HTTP_200_OK,
    summary="Get a silly walk grant application by ID",
    description="Retrieves detailed information about a specific silly walk grant application.",
    tags=["Applications"],
    responses={
        200: {"description": "Application retrieved successfully"},
        404: {"description": "Application not found"},
        500: {"description": "Internal server error"}
    }
)
def get_application_by_id(application_id: str):
    """
    Retrieve a silly walk grant application by its ID.
    
    Returns detailed information about the application, including its silliness score.
    """
    try:
        application = get_application(application_id)
        return application
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Application with ID {application_id} not found"
        ) from exc
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )

@router.get(
    "/applications",
    response_model=ApplicationListResponse,
    status_code=status.HTTP_200_OK,
    summary="List all silly walk grant applications",
    description="Retrieves a list of all silly walk grant applications with pagination support.",
    tags=["Applications"],
    responses={
        200: {"description": "Applications retrieved successfully"},
        500: {"description": "Internal server error"}
    }
)
def list_applications(
    skip: int = Query(0, ge=0, description="Number of applications to skip"),
    limit: int = Query(10, ge=1, le=100, description="Maximum number of applications to return")
):
    """
    List all silly walk grant applications with pagination support.
    
    Returns a paginated list of applications with basic details.
    """
    try:
        applications = get_all_applications(skip, limit)
        return applications
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred."
        )