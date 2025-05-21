"""
Unit tests for the application service.

This module tests the application service functionality.
"""

import unittest
from unittest.mock import patch, MagicMock
from app.services.application_service import create_application, get_application


class TestApplicationService(unittest.TestCase):
    """Test cases for the application service."""
    
    def setUp(self):
        """Set up for each test."""
        # Sample application data for testing
        self.test_application = {
            'applicant_name': 'John Cleese',
            'walk_name': 'Ministry Walk',
            'description': 'A very silly walk involving leg lifts and occasional hopping',
            'has_briefcase': True,
            'involves_hopping': True,
            'number_of_twirls': 3
        }
    
    @patch('app.services.application_service.calculate_silliness_score')
    @patch('app.services.application_service.store_application')
    @patch('uuid.uuid4')
    def test_create_application(self, mock_uuid, mock_store, mock_score):
        """Test application creation."""
        # Set up mocks
        mock_uuid.return_value = 'test-uuid-1234'
        mock_score.return_value = 42
        
        # Call function under test
        result = create_application(self.test_application)
        
        # Verify results
        self.assertEqual(result['application_id'], 'test-uuid-1234')
        self.assertEqual(result['silliness_score'], 42)
        self.assertEqual(result['status'], 'PendingReview')
        
        # Verify mocks were called correctly
        mock_score.assert_called_once_with(self.test_application)
        mock_store.assert_called_once()
    
    @patch('app.services.application_service.get_application_by_id')
    def test_get_application_found(self, mock_get_by_id):
        """Test application retrieval when found."""
        # Set up mock
        mock_application = MagicMock()
        mock_application.to_dict.return_value = {
            'id': 'test-uuid-1234',
            'applicant_name': 'John Cleese',
            'silliness_score': 42
        }
        mock_get_by_id.return_value = mock_application
        
        # Call function under test
        result = get_application('test-uuid-1234')
        
        # Verify results
        self.assertEqual(result['id'], 'test-uuid-1234')
        self.assertEqual(result['applicant_name'], 'John Cleese')
        self.assertEqual(result['silliness_score'], 42)
        
        # Verify mock was called correctly
        mock_get_by_id.assert_called_once_with('test-uuid-1234')
    
    @patch('app.services.application_service.get_application_by_id')
    def test_get_application_not_found(self, mock_get_by_id):
        """Test application retrieval when not found."""
        # Set up mock to return None (application not found)
        mock_get_by_id.return_value = None
        
        # Call function under test and check for exception
        with self.assertRaises(ValueError):
            get_application('nonexistent-uuid')
        
        # Verify mock was called correctly
        mock_get_by_id.assert_called_once_with('nonexistent-uuid')


if __name__ == '__main__':
    unittest.main()
