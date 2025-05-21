"""
Database models for application data.

This module contains the data models for silly walk applications.
"""

from datetime import datetime
from typing import Dict, Any, Optional


class ApplicationModel:
    """Model representing a silly walk grant application."""
    
    def __init__(
        self,
        id: str,
        applicant_name: str,
        walk_name: str,
        description: str,
        has_briefcase: bool,
        involves_hopping: bool,
        number_of_twirls: int,
        silliness_score: int,
        status: str,
        submission_timestamp: Optional[datetime] = None
    ):
        """
        Initialize an ApplicationModel instance.
        
        Args:
            id: Unique identifier for the application (UUID)
            applicant_name: Name of the applicant
            walk_name: Name of the silly walk
            description: Description of the silly walk
            has_briefcase: Whether the walk involves a briefcase
            involves_hopping: Whether the walk involves hopping
            number_of_twirls: Number of twirls in the walk
            silliness_score: Calculated silliness score
            status: Current status of the application
            submission_timestamp: When the application was submitted
        """
        self.id = id
        self.applicant_name = applicant_name
        self.walk_name = walk_name
        self.description = description
        self.has_briefcase = has_briefcase
        self.involves_hopping = involves_hopping
        self.number_of_twirls = number_of_twirls
        self.silliness_score = silliness_score
        self.status = status
        self.submission_timestamp = submission_timestamp or datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the model to a dictionary.
        
        Returns:
            Dict[str, Any]: Dictionary representation of the application
        """
        return {
            "id": self.id,
            "applicant_name": self.applicant_name,
            "walk_name": self.walk_name,
            "description": self.description,
            "has_briefcase": self.has_briefcase,
            "involves_hopping": self.involves_hopping,
            "number_of_twirls": self.number_of_twirls,
            "silliness_score": self.silliness_score,
            "status": self.status,
            "submission_timestamp": self.submission_timestamp.isoformat()
        }
