"""
Application service for the Silly Walk Grant Application Orchestrator.

This module contains functions for processing application submissions,
calculating scores, and persisting applications.
"""

import uuid
from datetime import datetime
from typing import Dict, Any, List

from app.models.applications import ApplicationModel
from app.services.scoring_service import calculate_silliness_score
from app.repositories.application_repository import store_application, get_application_by_id, get_all_applications as repo_get_all_applications


def create_application(application_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Process a new application submission.
    
    Args:
        application_data: Dictionary containing validated application data
        
    Returns:
        Dict[str, Any]: Dictionary with application_id, silliness_score, and status
    """
    # Generate a unique application ID
    application_id = str(uuid.uuid4())
    
    # Calculate the silliness score
    silliness_score = calculate_silliness_score(application_data)
    
    # Create an application model for storage
    application = ApplicationModel(
        id=application_id,
        applicant_name=application_data.get('applicant_name'),
        walk_name=application_data.get('walk_name'),
        description=application_data.get('description'),
        has_briefcase=application_data.get('has_briefcase'),
        involves_hopping=application_data.get('involves_hopping'),
        number_of_twirls=application_data.get('number_of_twirls'),
        silliness_score=silliness_score,
        status="PendingReview",
        submission_timestamp=datetime.now()
    )
    
    # Store the application
    store_application(application)
    
    # Return the response data
    return {
        "application_id": application_id,
        "silliness_score": silliness_score,
        "status": "PendingReview"
    }


def get_application(application_id: str) -> Dict[str, Any]:
    """
    Retrieve an application by its ID.
    
    Args:
        application_id: The UUID of the application to retrieve
        
    Returns:
        Dict[str, Any]: Application data
        
    Raises:
        ValueError: If the application ID is invalid or application not found
    """
    try:
        application = get_application_by_id(application_id)
        if not application:
            raise ValueError(f"Application with ID {application_id} not found")
        return application.to_dict()
    except Exception as e:
        raise ValueError(f"Error retrieving application: {str(e)}")


def get_all_applications(skip: int = 0, limit: int = 10) -> Dict[str, Any]:
    """
    Retrieve all applications with pagination support.
    
    Args:
        skip: Number of applications to skip
        limit: Maximum number of applications to return
        
    Returns:
        Dict[str, Any]: Dictionary with applications list and total count
    """
    applications = repo_get_all_applications()
    total = len(applications)
    
    # Apply pagination
    paginated_applications = applications[skip:skip + limit]
    
    # Convert to dictionaries
    application_dicts = [app.to_dict() for app in paginated_applications]
    
    return {
        "applications": application_dicts,
        "total": total
    }
