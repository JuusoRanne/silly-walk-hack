"""
Scoring service for silly walk applications.

This module contains functions for calculating the silliness score of walk applications
based on predefined criteria.
"""

import re
from typing import Dict, Any, List, Set


class ScoringService:
    """Service for calculating silliness scores for walk applications."""

    def __init__(self):
        """Initialize the scoring service with an empty set of walk names."""
        self._walk_names: Set[str] = set()

    def calculate_silliness_score(self, application: Dict[str, Any]) -> int:
        """
        Calculate the silliness score for a walk application based on predefined rules.
        
        Args:
            application: Dictionary containing application data with at least
                        'description', 'has_briefcase', 'walk_name', and 'number_of_twirls'
        
        Returns:
            int: The calculated silliness score
        
        Rules:
        - Base score: 10 points if description is longer than 20 characters
        - Briefcase bonus: +5 points if has_briefcase is true
        - Hopping bonus: +3 points per "hop"/"hopping" in description (max 15 points)
        - Twirltastic score: +2 points per twirl (max 20 points)
        - Originality factor: +7 points if walk_name is unique
        """
        score = 0
        
        # Base score: 10 points if description is longer than 20 characters
        description = application.get('description', '')
        if len(description) > 20:
            score += 10
            
        # Briefcase bonus: +5 points if has_briefcase is true
        if application.get('has_briefcase', False):
            score += 5
            
        # Hopping bonus: +3 points for each instance of the word "hop" or "hopping"
        # (case-insensitive) in the description, up to a maximum of 15 points
        hop_count = self._count_hop_instances(description)
        hopping_points = min(hop_count * 3, 15)
        score += hopping_points
            
        # Twirltastic score: +2 points for every number_of_twirls, max 20 points
        twirls = application.get('number_of_twirls', 0)
        twirl_points = min(twirls * 2, 20)
        score += twirl_points
            
        # Originality factor: +7 points if walk_name is unique
        walk_name = application.get('walk_name', '').lower()
        if walk_name and walk_name not in self._walk_names:
            score += 7
            self._walk_names.add(walk_name)
            
        return score
    
    def _count_hop_instances(self, description: str) -> int:
        """
        Count the occurrences of "hop" and "hopping" in the description.
        
        Args:
            description: The walk description text
            
        Returns:
            int: Count of hop/hopping instances
        """
        if not description:
            return 0
            
        # Case-insensitive search for "hop" and "hopping"
        # Using regex with word boundaries to match whole words only
        hop_pattern = r'\bhop(?:ping)?\b'
        matches = re.findall(hop_pattern, description.lower())
        return len(matches)
    
    def reset_walk_names(self) -> None:
        """Reset the set of known walk names (primarily for testing)."""
        self._walk_names = set()


# Create a singleton instance to be used throughout the application
scoring_service = ScoringService()


def calculate_silliness_score(application: Dict[str, Any]) -> int:
    """
    Calculate the silliness score for a walk application.
    
    This is the public function that should be imported and used by other modules.
    
    Args:
        application: Dictionary containing application data
        
    Returns:
        int: The calculated silliness score
    """
    return scoring_service.calculate_silliness_score(application)
