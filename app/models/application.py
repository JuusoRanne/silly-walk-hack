"""
SQLAlchemy models for the application.

This module defines the database models using SQLAlchemy ORM.
"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base

class Application(Base):
    """
    SQLAlchemy model for the silly walk grant application.
    """
    __tablename__ = "applications"

    # Use UUID for primary key to prevent sequential ID enumeration
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)

    # Application details
    applicant_name = Column(String(100), nullable=False)
    walk_name = Column(String(100), nullable=False, index=True)
    description = Column(Text, nullable=False)
    has_briefcase = Column(Boolean, nullable=False, default=False)
    involves_hopping = Column(Boolean, nullable=False, default=False)
    number_of_twirls = Column(Integer, nullable=False, default=0)

    # Calculated fields
    silliness_score = Column(Integer, nullable=False, default=0)

    # Status and timestamps
    status = Column(String(50), nullable=False, default="PendingReview")
    submission_timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<Application {self.id}: {self.walk_name} by {self.applicant_name}>"
