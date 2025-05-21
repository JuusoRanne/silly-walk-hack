"""
Main entry point for the Silly Walk Grant Application Orchestrator API.

This module initializes the FastAPI application, configures middleware,
registers routers, and sets up exception handlers.
"""
import os
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.openapi.utils import get_openapi
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import routers
from app.routes import application_routes
from app.db.database import create_tables
from app.utils.error_handlers import setup_exception_handlers

# Create FastAPI app
app = FastAPI(
    title="Silly Walk Grant Application Orchestrator",
    description="A secure backend API service for managing silly walk grant applications.",
    version="1.0.0",
    docs_url=None,  # Disable default docs URL to customize it
    redoc_url=None  # Disable default redoc URL to customize it
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, this should be restricted to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Content-Type-Options", "X-Frame-Options"]
)

# Add security headers middleware
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    # In a real production environment, we'd also add:
    # Strict-Transport-Security: max-age=31536000; includeSubDomains
    return response

# Set up custom exception handlers
setup_exception_handlers(app)

# Include routers
app.include_router(application_routes.router, prefix="/api/v1", tags=["applications"])

# Health check endpoint
@app.get("/health", status_code=status.HTTP_200_OK, tags=["health"])
async def health_check():
    """
    Health check endpoint to verify API is running.

    Returns:
        dict: Status message indicating the API is operational
    """
    return {"status": "healthy", "message": "The Silly Walk Grant Application Orchestrator API is running"}

# Custom OpenAPI documentation endpoints
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    """
    Custom Swagger UI endpoint with security headers.
    """
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
    )

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    """
    Custom ReDoc endpoint with security headers.
    """
    return get_redoc_html(
        openapi_url="/openapi.json",
        title=app.title + " - ReDoc",
        redoc_js_url="https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js",
    )

# Custom OpenAPI schema to add security scheme
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    # Add API key security scheme
    openapi_schema["components"] = openapi_schema.get("components", {})
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

# Create tables on startup
@app.on_event("startup")
async def startup_event():
    """
    Execute actions on application startup.
    """
    # Create database tables
    create_tables()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
