"""
Unit tests for the scoring service.

This module tests the silliness score calculation algorithm.
"""

import unittest
from app.services.scoring_service import ScoringService


class TestScoringService(unittest.TestCase):
    """Test cases for the ScoringService class."""
    
    def setUp(self):
        """Set up a new ScoringService instance for each test."""
        self.scoring_service = ScoringService()
    
    def test_base_score(self):
        """Test the base score calculation (10 points if description > 20 chars)."""
        # Short description (≤ 20 chars)
        application_short = {
            'description': 'Short desc',
            'has_briefcase': False,
            'number_of_twirls': 0,
            'walk_name': 'Test Walk Short'
        }
        score_short = self.scoring_service.calculate_silliness_score(application_short)
        self.assertEqual(score_short, 7)  # Only originality bonus (7 points)
        
        # Long description (> 20 chars)
        application_long = {
            'description': 'This description is definitely longer than twenty characters',
            'has_briefcase': False,
            'number_of_twirls': 0,
            'walk_name': 'Test Walk Long'
        }
        score_long = self.scoring_service.calculate_silliness_score(application_long)
        self.assertEqual(score_long, 17)  # Base score (10) + originality bonus (7)
    
    def test_briefcase_bonus(self):
        """Test the briefcase bonus (5 points if has_briefcase is true)."""
        # Without briefcase
        application_no_briefcase = {
            'description': 'Test description',
            'has_briefcase': False,
            'number_of_twirls': 0,
            'walk_name': 'No Briefcase Walk'
        }
        score_no_briefcase = self.scoring_service.calculate_silliness_score(application_no_briefcase)
        
        # With briefcase
        application_with_briefcase = {
            'description': 'Test description',
            'has_briefcase': True,
            'number_of_twirls': 0,
            'walk_name': 'Briefcase Walk'
        }
        score_with_briefcase = self.scoring_service.calculate_silliness_score(application_with_briefcase)
        
        # Difference should be exactly 5 points (briefcase bonus)
        self.assertEqual(score_with_briefcase - score_no_briefcase, 5)
    
    def test_hopping_bonus(self):
        """Test the hopping bonus (3 points per hop/hopping, max 15)."""
        # No hopping
        application_no_hop = {
            'description': 'Walking normally with no special movements',
            'has_briefcase': False,
            'number_of_twirls': 0,
            'walk_name': 'No Hop Walk'
        }
        score_no_hop = self.scoring_service.calculate_silliness_score(application_no_hop)
        self.assertEqual(score_no_hop, 17)  # Base (10) + originality (7)
        
        # One hop
        application_one_hop = {
            'description': 'Walking with one hop in the middle',
            'has_briefcase': False,
            'number_of_twirls': 0,
            'walk_name': 'One Hop Walk'
        }
        score_one_hop = self.scoring_service.calculate_silliness_score(application_one_hop)
        self.assertEqual(score_one_hop, 20)  # Base (10) + hop (3) + originality (7)
        
        # Multiple hops (max bonus)
        application_many_hops = {
            'description': 'Hop hop hop hop hop hopping all day long with continuous hopping motions',
            'has_briefcase': False,
            'number_of_twirls': 0,
            'walk_name': 'Many Hops Walk'
        }
        score_many_hops = self.scoring_service.calculate_silliness_score(application_many_hops)
        self.assertEqual(score_many_hops, 42)  # Base (10) + max hop bonus (15) + originality (7) + description (10)
    
    def test_twirl_score(self):
        """Test the twirltastic score (2 points per twirl, max 20)."""
        # No twirls
        application_no_twirls = {
            'description': 'Test description',
            'has_briefcase': False,
            'number_of_twirls': 0,
            'walk_name': 'No Twirls Walk'
        }
        score_no_twirls = self.scoring_service.calculate_silliness_score(application_no_twirls)
        
        # 5 twirls
        application_five_twirls = {
            'description': 'Test description',
            'has_briefcase': False,
            'number_of_twirls': 5,
            'walk_name': 'Five Twirls Walk'
        }
        score_five_twirls = self.scoring_service.calculate_silliness_score(application_five_twirls)
        
        # Difference should be 10 points (5 twirls × 2 points)
        self.assertEqual(score_five_twirls - score_no_twirls, 10)
        
        # Many twirls (testing max cap)
        application_many_twirls = {
            'description': 'Test description',
            'has_briefcase': False,
            'number_of_twirls': 20,  # 20 twirls = 40 points, but capped at 20
            'walk_name': 'Many Twirls Walk'
        }
        score_many_twirls = self.scoring_service.calculate_silliness_score(application_many_twirls)
        
        # Difference from no twirls should be 20 (max twirl bonus)
        self.assertEqual(score_many_twirls - score_no_twirls, 20)
    
    def test_originality_factor(self):
        """Test the originality factor (7 points if walk_name is unique)."""
        # First submission of a walk name gets originality bonus
        application_first = {
            'description': 'Test description',
            'has_briefcase': False,
            'number_of_twirls': 0,
            'walk_name': 'Unique Walk Name'
        }
        score_first = self.scoring_service.calculate_silliness_score(application_first)
        
        # Second submission of the same walk name doesn't get originality bonus
        application_duplicate = {
            'description': 'Another test description',
            'has_briefcase': False,
            'number_of_twirls': 0,
            'walk_name': 'Unique Walk Name'  # Same name as before
        }
        score_duplicate = self.scoring_service.calculate_silliness_score(application_duplicate)
        
        # First submission should have 7 more points than the duplicate
        self.assertEqual(score_first - score_duplicate, 7)
    
    def test_combined_score(self):
        """Test a combination of all scoring factors."""
        application = {
            'description': 'This silly walk involves hopping on one leg while hopping the briefcase up and down',
            'has_briefcase': True,
            'number_of_twirls': 8,
            'walk_name': 'The Ultimate Silly Walk'
        }
        score = self.scoring_service.calculate_silliness_score(application)
        
        # Expected: Base (10) + briefcase (5) + hopping (2 × 3 = 6) + twirls (8 × 2 = 16) + originality (7) = 44
        self.assertEqual(score, 44)
    
    def tearDown(self):
        """Clean up after each test."""
        self.scoring_service.reset_walk_names()


if __name__ == '__main__':
    unittest.main()
