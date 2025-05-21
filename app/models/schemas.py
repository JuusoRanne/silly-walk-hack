"""
Pydantic models for request/response validation and serialization.

This module defines the schemas used for validating API requests and formatting responses.
"""
from pydantic import BaseModel, Field, validator
from typing import Optional
from uuid import UUID
from datetime import datetime
import re

class ApplicationBase(BaseModel):
    """
    Base schema with shared attributes for the Application entity.
    """
    applicant_name: str = Field(
        ...,
        description="Name of the applicant",
        min_length=1,
        max_length=100,
        example="John Cleese"
    )
    walk_name: str = Field(
        ...,
        description="Name of the silly walk",
        min_length=1,
        max_length=100,
        example="The Ministry Walk"
    )
    description: str = Field(
        ...,
        description="Description of the walk's silliness",
        min_length=1,
        example="A very silly walk involving high leg lifts and hopping"
    )
    has_briefcase: bool = Field(
        ...,
        description="Whether the walk involves a briefcase",
        example=True
    )
    involves_hopping: bool = Field(
        ...,
        description="Whether the walk involves hopping",
        example=True
    )
    number_of_twirls: int = Field(
        ...,
        description="Number of twirls in the walk",
        ge=0,
        example=3
    )

    # Additional validators for security
    @validator('applicant_name', 'walk_name')
    def validate_names(cls, v):
        """Validate name fields for security."""
        if not v.strip():
            raise ValueError("Field cannot be empty or just whitespace")

        # Prevent potential HTML/script injection
        if re.search(r'<[^>]*>', v):
            raise ValueError("HTML tags are not allowed")

        return v

    @validator('description')
    def validate_description(cls, v):
        """Validate description field for security."""
        if not v.strip():
            raise ValueError("Description cannot be empty or just whitespace")

        # Prevent potential HTML/script injection
        if re.search(r'<[^>]*>', v):
            raise ValueError("HTML tags are not allowed")

        return v

    @validator('number_of_twirls')
    def validate_twirls(cls, v):
        """Validate number_of_twirls for reasonableness."""
        if v > 100:
            raise ValueError("Number of twirls must be between 0 and 100")
        return v

class ApplicationCreate(ApplicationBase):
    """
    Schema for creating a new application.
    """
    pass

class ApplicationStatus(BaseModel):
    """
    Schema for updating application status.
    """
    status: str = Field(
        ...,
        description="Status of the application",
        example="ApprovedForFunding"
    )

    @validator('status')
    def validate_status(cls, v):
        """Validate that status is one of the allowed values."""
        allowed_statuses = [
            "PendingReview",
            "UnderSillyCouncilReview",
            "ApprovedForFunding",
            "RegrettablyNotSillyEnough"
        ]
        if v not in allowed_statuses:
            raise ValueError(f"Status must be one of: {', '.join(allowed_statuses)}")
        return v

class ApplicationUpdate(BaseModel):
    """
    Schema for updating an application.
    """
    applicant_name: Optional[str] = Field(
        None,
        description="Name of the applicant",
        min_length=1,
        max_length=100
    )
    walk_name: Optional[str] = Field(
        None,
        description="Name of the silly walk",
        min_length=1,
        max_length=100
    )
    description: Optional[str] = Field(
        None,
        description="Description of the walk's silliness",
        min_length=1
    )
    has_briefcase: Optional[bool] = Field(
        None,
        description="Whether the walk involves a briefcase"
    )
    involves_hopping: Optional[bool] = Field(
        None,
        description="Whether the walk involves hopping"
    )
    number_of_twirls: Optional[int] = Field(
        None,
        description="Number of twirls in the walk",
        ge=0
    )
    status: Optional[str] = Field(
        None,
        description="Status of the application"
    )

    # Use the same validators from ApplicationBase
    _validate_names = validator('applicant_name', 'walk_name', allow_reuse=True)(ApplicationBase.validate_names)
    _validate_description = validator('description', allow_reuse=True)(ApplicationBase.validate_description)
    _validate_twirls = validator('number_of_twirls', allow_reuse=True)(ApplicationBase.validate_twirls)
    _validate_status = validator('status', allow_reuse=True)(ApplicationStatus.validate_status)

class ApplicationResponse(ApplicationBase):
    """
    Schema for application response.
    """
    id: UUID = Field(..., description="Unique identifier for the application")
    silliness_score: int = Field(..., description="Calculated silliness score")
    status: str = Field(..., description="Status of the application")
    submission_timestamp: datetime = Field(..., description="When the application was submitted")

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "applicant_name": "John Cleese",
                "walk_name": "The Ministry Walk",
                "description": "A very silly walk involving high leg lifts and hopping",
                "has_briefcase": True,
                "involves_hopping": True,
                "number_of_twirls": 3,
                "silliness_score": 35,
                "status": "PendingReview",
                "submission_timestamp": "2023-07-14T12:34:56.789Z"
            }
        }
