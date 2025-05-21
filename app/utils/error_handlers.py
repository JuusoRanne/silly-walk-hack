"""
Custom exception handlers for the application.

This module provides centralized error handling to ensure consistent
error responses that don't leak sensitive information.
"""
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
from pydantic import ValidationError
import logging

# Set up logging
logger = logging.getLogger(__name__)

def setup_exception_handlers(app: FastAPI):
    """
    Register exception handlers with the FastAPI application.

    Args:
        app (FastAPI): The FastAPI application instance
    """

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """
        Handle validation errors from FastAPI/Pydantic.

        Args:
            request (Request): The request that caused the exception
            exc (RequestValidationError): The validation error

        Returns:
            JSONResponse: A formatted error response
        """
        # Log detailed error but return safe error message
        logger.error(f"Validation error: {exc.errors()}")

        # Extract error details for the response
        # This is safe to return as it only includes submitted data issues, not internal logic
        errors = []
        for error in exc.errors():
            error_msg = {
                "loc": error.get("loc", []),
                "msg": error.get("msg", ""),
                "type": error.get("type", "")
            }
            errors.append(error_msg)

        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": "error",
                "message": "Validation error in request data",
                "errors": errors
            }
        )

    @app.exception_handler(SQLAlchemyError)
    async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
        """
        Handle database errors.

        Args:
            request (Request): The request that caused the exception
            exc (SQLAlchemyError): The database error

        Returns:
            JSONResponse: A generic error response
        """
        # Log detailed error but return generic message
        logger.error(f"Database error: {str(exc)}")

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status": "error",
                "message": "A database error occurred"
            }
        )

    @app.exception_handler(ValueError)
    async def value_error_handler(request: Request, exc: ValueError):
        """
        Handle value errors.

        Args:
            request (Request): The request that caused the exception
            exc (ValueError): The value error

        Returns:
            JSONResponse: A formatted error response
        """
        logger.error(f"Value error: {str(exc)}")

        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "status": "error",
                "message": str(exc)
            }
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        """
        Handle any unhandled exceptions.

        Args:
            request (Request): The request that caused the exception
            exc (Exception): The exception

        Returns:
            JSONResponse: A generic error response
        """
        # Log detailed error but return generic message
        logger.error(f"Unhandled exception: {str(exc)}")

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status": "error",
                "message": "An unexpected error occurred"
            }
        )
