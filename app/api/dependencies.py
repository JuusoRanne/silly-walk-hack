"""
API dependencies for authentication and other middleware functions.

This module provides dependencies that can be used with FastAPI endpoints.
"""

from fastapi import Header, HTTPException, status


# For demonstration purposes, this is a hardcoded API key
# In a production environment, this would be securely stored
# in environment variables or a secrets manager
API_KEY = "SILLY_WALKS_2023_SECRET_KEY"


async def verify_api_key(x_api_key: str = Header(..., description="API key for authentication")) -> str:
    """
    Verify the API key provided in the X-API-Key header.
    
    Args:
        x_api_key: The API key from the request header
        
    Returns:
        str: The validated API key
        
    Raises:
        HTTPException: If the API key is missing or invalid
    """
    if not x_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key is required",
            headers={"WWW-Authenticate": "ApiKey"}
        )
        
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "ApiKey"}
        )
        
    return x_api_key
