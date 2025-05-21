"""
Repository for application data persistence.

This module provides functions to store and retrieve applications from the data store.
For this MVP, a simple in-memory storage solution is implemented.
"""

from typing import Dict, List, Optional
from app.models.applications import ApplicationModel


# In-memory storage for applications
# In a production environment, this would be replaced with a database
_applications: Dict[str, ApplicationModel] = {}


def store_application(application: ApplicationModel) -> None:
    """
    Store an application in the data store.
    
    Args:
        application: The ApplicationModel instance to store
    """
    _applications[application.id] = application


def get_application_by_id(application_id: str) -> Optional[ApplicationModel]:
    """
    Retrieve an application by its ID.
    
    Args:
        application_id: The unique identifier of the application
        
    Returns:
        Optional[ApplicationModel]: The application if found, None otherwise
    """
    return _applications.get(application_id)


def get_all_applications() -> List[ApplicationModel]:
    """
    Retrieve all applications from the data store.
    
    Returns:
        List[ApplicationModel]: List of all applications
    """
    return list(_applications.values())
