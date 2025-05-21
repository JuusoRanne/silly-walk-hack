"""
Scoring service for silly walk grant applications.

This module implements the algorithm to calculate the "silliness score" of walk applications
based on the criteria defined in the project specifications.
"""
import re
from typing import Optional
from sqlalchemy.orm import Session
from app.db.repository import ApplicationRepository
from app.models.schemas import ApplicationCreate

class ScoringService:
    """
    Service for calculating silliness scores for walk applications.
    """

    @staticmethod
    def calculate_score(
        application: ApplicationCreate,
        db: Session,
        check_uniqueness: bool = True
    ) -> int:
        """
        Calculate the silliness score for a walk application.

        The scoring algorithm is based on multiple factors:
        - Base score: 10 points if description is longer than 20 characters
        - Briefcase bonus: +5 points if application involves a briefcase
        - Hopping bonus: +3 points for each mention of "hop" or "hopping" in the description (max 15)
        - Twirltastic score: +2 points for each twirl, up to a maximum of 20 points
        - Originality bonus: +7 points if the walk name is unique

        Args:
            application (ApplicationCreate): The application to score
            db (Session): Database session for checking walk name uniqueness
            check_uniqueness (bool): Whether to check for name uniqueness (default: True)

        Returns:
            int: The calculated silliness score
        """
        score = 0

        # Base score: 10 points if description is longer than 20 characters
        if len(application.description) > 20:
            score += 10

        # Briefcase bonus: +5 points if application involves a briefcase
        if application.has_briefcase:
            score += 5

        # Hopping bonus: +3 points for each mention of "hop" or "hopping" in the description (max 15)
        hop_count = len(re.findall(r'\bhop(?:ping)?\b', application.description.lower()))
        hopping_bonus = min(hop_count * 3, 15)  # Cap at 15 points
        score += hopping_bonus

        # Twirltastic score: +2 points for each twirl, up to a maximum of 20 points
        twirl_points = min(application.number_of_twirls * 2, 20)  # Cap at 20 points
        score += twirl_points

        # Originality bonus: +7 points if the walk name is unique
        if check_uniqueness and ApplicationRepository.is_walk_name_unique(db, application.walk_name):
            score += 7

        return score
