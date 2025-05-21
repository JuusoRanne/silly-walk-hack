"""
Main application module for the Silly Walk Grant Application Orchestrator.

This module initializes the FastAPI application and includes all routes.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from app.api.routes.applications import router as applications_router


def create_application() -> FastAPI:
    """
    Create and configure a FastAPI application.
    
    Returns:
        FastAPI: Configured FastAPI application
    """
    app = FastAPI(
        title="Silly Walk Grant Application Orchestrator",
        description="A backend service for managing silly walk grant applications",
        version="1.0.0",
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, specify exact origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include routers
    app.include_router(applications_router, prefix="/api/v1")
    
    # Customize OpenAPI
    def custom_openapi():
        if app.openapi_schema:
            return app.openapi_schema
            
        openapi_schema = get_openapi(
            title=app.title,
            version=app.version,
            description=app.description,
            routes=app.routes,
        )
        
        # Security scheme for API key
        openapi_schema["components"]["securitySchemes"] = {
            "ApiKeyAuth": {
                "type": "apiKey",
                "in": "header",
                "name": "X-API-Key"
            }
        }
        
        app.openapi_schema = openapi_schema
        return app.openapi_schema
        
    app.openapi = custom_openapi
    
    return app


app = create_application()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
