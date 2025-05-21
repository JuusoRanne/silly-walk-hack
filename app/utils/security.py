"""
Security utilities for the application.

This module provides security-related utility functions for use throughout the application.
"""
import re
import logging
from typing import Optional

# Set up logging
logger = logging.getLogger(__name__)

def sanitize_log_data(data: dict) -> dict:
    """
    Sanitize sensitive data for logging purposes.

    This function replaces sensitive fields with placeholder values to prevent
    sensitive information from appearing in logs.

    Args:
        data (dict): The data to sanitize

    Returns:
        dict: Sanitized data safe for logging
    """
    if not data or not isinstance(data, dict):
        return data

    sensitive_fields = [
        "api_key",
        "password",
        "token",
        "secret",
        "credential"
    ]

    sanitized = data.copy()

    for field in sensitive_fields:
        for key in list(sanitized.keys()):
            if field.lower() in key.lower():
                sanitized[key] = "***REDACTED***"

    return sanitized

def validate_string_security(value: str, field_name: str,
                            min_length: int = 1,
                            max_length: int = 1000,
                            pattern: Optional[str] = None) -> bool:
    """
    Validate a string for security concerns.

    Performs validation on string fields to prevent injection attacks
    and ensure data quality.

    Args:
        value (str): The string to validate
        field_name (str): Name of the field (for error messages)
        min_length (int): Minimum allowed length
        max_length (int): Maximum allowed length
        pattern (Optional[str]): Optional regex pattern to enforce

    Returns:
        bool: True if the string passes all validations

    Raises:
        ValueError: If the string fails validation
    """
    # Check type
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be a string")

    # Check length
    if len(value) < min_length:
        raise ValueError(f"{field_name} must be at least {min_length} characters")

    if len(value) > max_length:
        raise ValueError(f"{field_name} must be no more than {max_length} characters")

    # Check pattern if provided
    if pattern and not re.match(pattern, value):
        raise ValueError(f"{field_name} does not match the required pattern")

    return True
