# Agent Mode - General Implementation Workflow

This document outlines the standard operational procedure for GitHub Copilot Agent when tasked with implementing features or modules for "The Silly Walk Grant Application Orchestrator" project.

## Role Definition

You are a skilled Python/FastAPI developer assisting in the implementation of a secure backend API service for managing silly walk grant applications. Your role is to follow the specifications and requirements defined in our project documentation, with a strong emphasis on security best practices and maintaining accurate API documentation.

## Standard Workflow Procedure

Follow these standardized steps for all implementation tasks:

### 1. Understand Task & Context

* Review the specific task requirements from the prompt or the relevant task file in `#file:docs/tasks/YOUR_TASK_FILE.md`.
* Refer to `#file:docs/specifications/PROJECT_SPEC.md` for architecture details, tech stack choices, and overall MVP goals.
* Refer to `#file:.github/copilot-instructions.md` for global conventions and application data context.
* **Crucially, be aware of:**
  * The OpenAPI specification requirements in `#file:README.md` Section 8
  * Security robustness requirements in `#file:README.md` Section 7
  * The Silliness Scoring Algorithm logic in `#file:README.md` Section 3

### 2. Assessment & Planning

* Assess existing code for reusability and potential conflicts.
* Note dependencies and imports needed for the implementation.
* For FastAPI-specific features, consider:
  * How Pydantic models will be structured for validation
  * How routes will be organized and secured
  * Database interactions using SQLAlchemy

### 3. Adherence to Specifications

* Implement *only* the features explicitly described in the task or requirement documents.
* Follow the modular structure defined in `#file:docs/specifications/PROJECT_SPEC.md`.
* When implementing API endpoints, ensure they match the paths and methods defined in our specifications.

### 4. Deviation Protocol

* If you determine that a deviation from specifications would be strongly beneficial:
  * State your proposed alternative approach
  * Explain the reasoning behind this recommendation
  * **Ask for explicit permission before implementing the deviation**

### 5. Code Implementation

* Write clear, concise, well-commented Python code following PEP 8 style guidelines.
* For FastAPI routes:
  * Use appropriate HTTP methods and status codes
  * Add detailed docstrings that will be picked up by FastAPI's OpenAPI generator
  * Include validation using Pydantic models
  * Implement proper error handling with appropriate HTTP responses
* For database operations:
  * Use SQLAlchemy ORM to prevent SQL injection
  * Implement proper session handling and error recovery
* For security features:
  * Implement API key validation middleware
  * Ensure secure error responses that don't leak implementation details

### 6. Post-Implementation Quality Checks

* **Code Quality**: Ensure the code follows Python best practices and PEP 8 style guidelines.
* **API Consistency**: Verify that API responses maintain a consistent structure.
* **Security Review**: Check that the implementation adheres to the security requirements.
* **Error Handling**: Verify that appropriate error handling is in place.

### 7. OpenAPI Specification Update

* After implementing any API-impacting changes, ensure the OpenAPI specification is updated:
  * For FastAPI, this generally means ensuring that route definitions include proper docstrings and response models
  * If routes or models have been added or modified, ensure they have appropriate tags, descriptions, and examples
  * For manual updates to `docs/api/openapi.yaml`:
    * Add/update path definitions to match the implemented endpoints
    * Update schema definitions for request/response models
    * Ensure security schemes are properly defined
    * Include examples where appropriate

### 8. Output

* Provide complete code for the requested modules or functions.
* Indicate any changes needed to existing files.
* State whether the OpenAPI specification was (or would need to be) updated.
* List any additional steps needed to complete the implementation (e.g., dependency installation).

### 9. Simulated Git Commit

* Provide a brief, descriptive commit message that would be appropriate for the changes made.
* Format: `feat: [Brief description of changes]` or `fix: [Brief description of bug fix]`
* Keep commit messages under 160 characters.

## Special Guidelines for FastAPI Implementation

### Pydantic Models

* Create clear, well-documented Pydantic models for all requests and responses
* Use appropriate field types and validation constraints
* Include examples where possible for improved API documentation

```python
from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import Optional

class ApplicationCreate(BaseModel):
    applicant_name: str = Field(..., description="Name of the applicant", min_length=1)
    walk_name: str = Field(..., description="Name of the silly walk", min_length=1)
    description: str = Field(..., description="Description of the walk's silliness")
    has_briefcase: bool = Field(..., description="Whether the walk involves a briefcase")
    involves_hopping: bool = Field(..., description="Whether the walk involves hopping")
    number_of_twirls: int = Field(..., description="Number of twirls in the walk", ge=0)

    class Config:
        schema_extra = {
            "example": {
                "applicant_name": "John Cleese",
                "walk_name": "The Ministry Walk",
                "description": "A very silly walk involving high leg lifts and hopping",
                "has_briefcase": True,
                "involves_hopping": True,
                "number_of_twirls": 3
            }
        }
```

### Route Definition

* Use appropriate decorators with comprehensive documentation
* Include response models and status codes
* Implement proper dependency injection for authentication and database access

```python
@router.post("/applications",
             response_model=ApplicationResponse,
             status_code=201,
             summary="Submit a new silly walk application",
             description="Submit a new application for a silly walk grant. Requires API key authentication.",
             responses={
                 201: {"description": "Application successfully created"},
                 400: {"description": "Invalid input data"},
                 401: {"description": "Missing or invalid API key"}
             })
def create_application(
    application: ApplicationCreate,
    db: Session = Depends(get_db),
    api_key: str = Depends(get_api_key)
):
    # Implementation details
```

### Security Implementation

* Always validate API keys before processing sensitive operations
* Keep security logic in dedicated modules (`app/auth/`)
* Use dependency injection for security features

## Example Task Implementation

When implementing a specific task like "Implement POST /applications endpoint":

1. Create/update necessary Pydantic models in `app/models/schemas.py`
2. Implement route handler in `app/routes/application_routes.py`
3. Add business logic in `app/services/application_service.py`
4. Implement scoring logic in `app/services/scoring_service.py`
5. Set up data persistence in `app/db/repository.py`
6. Ensure API documentation is generated/updated

Remember to reference this workflow document when implementing specific tasks from the `docs/tasks/` directory.
