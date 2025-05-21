"""
API key authentication implementation.

This module provides functions for validating API keys for protected endpoints.
"""
import os
import secrets
from fastapi import HTTPException, Security, status, Depends, Header
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv
import logging

# Set up logging
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Get API key from environment or use a default for development only
API_KEY = os.getenv("SILLY_WALK_API_KEY", "development_api_key_replace_in_production")

# Define API key header scheme
api_key_header = APIKeyHeader(name="X-API-Key")

def get_api_key(api_key: str = Security(api_key_header)) -> str:
    """
    Validate the API key provided in the X-API-Key header.

    This dependency function can be used to protect endpoints that require authentication.
    It performs a secure, constant-time comparison of the provided API key with the
    expected API key to prevent timing attacks.

    Args:
        api_key (str): API key from the X-API-Key header

    Returns:
        str: The validated API key

    Raises:
        HTTPException: 401 if API key is missing or invalid
    """
    if not api_key:
        logger.warning("API key missing in request")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key is required",
            headers={"WWW-Authenticate": "ApiKey"},
        )

    # Use constant-time comparison to prevent timing attacks
    if not secrets.compare_digest(api_key, API_KEY):
        logger.warning("Invalid API key provided")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "ApiKey"},
        )

    return api_key
