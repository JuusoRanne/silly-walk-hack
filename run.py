"""
Entry point for the Silly Walk Grant Application Orchestrator.

This module provides a simple way to run the application.
"""

import uvicorn
from app.main import app


def run_application():
    """Run the FastAPI application."""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    run_application()
