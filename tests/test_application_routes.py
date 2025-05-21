"""
Tests for the API routes.

This module tests the FastAPI routes using TestClient.
"""

import unittest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.main import app


class TestApplicationRoutes(unittest.TestCase):
    """Test cases for the application routes."""
    
    def setUp(self):
        """Set up for each test."""
        self.client = TestClient(app)
        self.api_key = "SILLY_WALKS_2023_SECRET_KEY"
        self.valid_application = {
            "applicant_name": "John Cleese",
            "walk_name": "Ministry Walk",
            "description": "A very silly walk involving leg lifts and occasional hopping",
            "has_briefcase": True,
            "involves_hopping": True,
            "number_of_twirls": 3
        }
    
    @patch('app.api.routes.applications.create_application')
    def test_submit_application_success(self, mock_create_application):
        """Test successful application submission."""
        # Set up mock
        mock_create_application.return_value = {
            "application_id": "test-uuid-1234",
            "silliness_score": 42,
            "status": "PendingReview"
        }
        
        # Call API endpoint
        response = self.client.post(
            "/api/v1/applications",
            json=self.valid_application,
            headers={"X-API-Key": self.api_key}
        )
        
        # Verify response
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["application_id"], "test-uuid-1234")
        self.assertEqual(response.json()["silliness_score"], 42)
        self.assertEqual(response.json()["status"], "PendingReview")
        
        # Verify mock was called correctly
        mock_create_application.assert_called_once()
    
    def test_submit_application_missing_api_key(self):
        """Test application submission without API key."""
        # Call API endpoint without API key
        response = self.client.post(
            "/api/v1/applications",
            json=self.valid_application
        )
        
        # Verify response indicates authentication error
        self.assertEqual(response.status_code, 401)
    
    def test_submit_application_invalid_api_key(self):
        """Test application submission with invalid API key."""
        # Call API endpoint with invalid API key
        response = self.client.post(
            "/api/v1/applications",
            json=self.valid_application,
            headers={"X-API-Key": "invalid-key"}
        )
        
        # Verify response indicates forbidden
        self.assertEqual(response.status_code, 403)
    
    def test_submit_application_invalid_data(self):
        """Test application submission with invalid data."""
        # Create invalid application missing required fields
        invalid_application = {
            "applicant_name": "",  # Empty name (invalid)
            "walk_name": "Test Walk"
            # Missing required fields
        }
        
        # Call API endpoint
        response = self.client.post(
            "/api/v1/applications",
            json=invalid_application,
            headers={"X-API-Key": self.api_key}
        )
        
        # Verify response indicates bad request
        self.assertEqual(response.status_code, 422)  # Validation error
    
    @patch('app.api.routes.applications.get_application')
    def test_get_application_by_id_success(self, mock_get_application):
        """Test successful application retrieval."""
        # Set up mock
        mock_get_application.return_value = {
            "id": "test-uuid-1234",
            "applicant_name": "John Cleese",
            "walk_name": "Ministry Walk",
            "description": "A very silly walk",
            "has_briefcase": True,
            "involves_hopping": True,
            "number_of_twirls": 3,
            "silliness_score": 42,
            "status": "PendingReview",
            "submission_timestamp": "2023-05-21T14:30:00"
        }
        
        # Call API endpoint
        response = self.client.get("/api/v1/applications/test-uuid-1234")
        
        # Verify response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], "test-uuid-1234")
        self.assertEqual(response.json()["applicant_name"], "John Cleese")
        self.assertEqual(response.json()["silliness_score"], 42)
        
        # Verify mock was called correctly
        mock_get_application.assert_called_once_with("test-uuid-1234")
    
    @patch('app.api.routes.applications.get_application')
    def test_get_application_by_id_not_found(self, mock_get_application):
        """Test application retrieval when not found."""
        # Set up mock to raise ValueError (application not found)
        mock_get_application.side_effect = ValueError("Application not found")
        
        # Call API endpoint
        response = self.client.get("/api/v1/applications/nonexistent-uuid")
        
        # Verify response indicates not found
        self.assertEqual(response.status_code, 404)
        
        # Verify mock was called correctly
        mock_get_application.assert_called_once_with("nonexistent-uuid")
    
    @patch('app.api.routes.applications.get_all_applications')
    def test_list_applications_success(self, mock_get_all_applications):
        """Test successful applications listing."""
        # Set up mock
        mock_get_all_applications.return_value = {
            "applications": [
                {
                    "id": "test-uuid-1",
                    "applicant_name": "John Cleese",
                    "walk_name": "Ministry Walk",
                    "description": "A very silly walk",
                    "has_briefcase": True,
                    "involves_hopping": True,
                    "number_of_twirls": 3,
                    "silliness_score": 42,
                    "status": "PendingReview",
                    "submission_timestamp": "2023-05-21T14:30:00"
                },
                {
                    "id": "test-uuid-2",
                    "applicant_name": "Michael Palin",
                    "walk_name": "Silly Strut",
                    "description": "Another silly walk",
                    "has_briefcase": False,
                    "involves_hopping": True,
                    "number_of_twirls": 5,
                    "silliness_score": 35,
                    "status": "PendingReview",
                    "submission_timestamp": "2023-05-21T15:45:00"
                }
            ],
            "total": 2
        }
        
        # Call API endpoint
        response = self.client.get("/api/v1/applications")
        
        # Verify response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["applications"]), 2)
        self.assertEqual(response.json()["total"], 2)
        self.assertEqual(response.json()["applications"][0]["applicant_name"], "John Cleese")
        self.assertEqual(response.json()["applications"][1]["applicant_name"], "Michael Palin")
        
        # Verify mock was called correctly
        mock_get_all_applications.assert_called_once_with(0, 10)
    
    @patch('app.api.routes.applications.get_all_applications')
    def test_list_applications_with_pagination(self, mock_get_all_applications):
        """Test applications listing with pagination parameters."""
        # Set up mock
        mock_get_all_applications.return_value = {
            "applications": [],
            "total": 50
        }
        
        # Call API endpoint with pagination parameters
        response = self.client.get("/api/v1/applications?skip=20&limit=5")
        
        # Verify response
        self.assertEqual(response.status_code, 200)
        
        # Verify mock was called correctly with pagination parameters
        mock_get_all_applications.assert_called_once_with(20, 5)


if __name__ == '__main__':
    unittest.main()
