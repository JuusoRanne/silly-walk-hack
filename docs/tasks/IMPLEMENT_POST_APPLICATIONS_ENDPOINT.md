# Task: Implement POST /applications Endpoint

**Workflow Reference:** When implementing this task, adhere to the general procedure outlined in #file:docs/instructions/agent_workflow.md. **Pay special attention to the OpenAPI Specification Update step.**

**Project Specification Reference:** #file:docs/specifications/PROJECT_SPEC.md
**Architecture Reference:** #file:docs/specifications/ARCHITECTURE.md
**README.md References:** Section 2 (Business Requirements, esp. #1, #2, #3, #4), Section 7 (Security Robustness), Section 8 (OpenAPI)
**Target Modules:**
- `app/routes/application_routes.py`
- `app/services/application_service.py`
- `app/services/scoring_service.py`
- `app/models/schemas.py` (update if needed)
**Assigned Role:** Backend API Developer with a focus on security and documentation

## Goal
Implement the `POST /applications` endpoint to allow submission of new silly walk grant applications, including input validation, API key authentication, silliness scoring, data persistence, and ensuring the OpenAPI specification is updated.

---

## Specific Requirements & Acceptance Criteria

### 1. Endpoint Definition and Authentication

Create a `POST /applications` endpoint with:

- Proper FastAPI route decorator with comprehensive documentation
- API key authentication using the dependency from `app/auth/api_key_auth.py`
- Appropriate HTTP status codes:
  - 201 Created (success)
  - 400 Bad Request (validation error)
  - 401 Unauthorized (missing API key)
  - 403 Forbidden (invalid API key)
  - 500 Internal Server Error (with non-revealing message)

### 2. Request Validation

Implement thorough request validation for the application submission:

- Use Pydantic models from `app/models/schemas.py` for validation
- Validate that all required fields are present:
  - `applicant_name` (string, non-empty)
  - `walk_name` (string, non-empty)
  - `description` (string)
  - `has_briefcase` (boolean)
  - `involves_hopping` (boolean)
  - `number_of_twirls` (integer, non-negative)
- Include detailed validation error messages that are helpful but don't leak implementation details

### 3. Silliness Scoring Implementation

Implement the scoring algorithm in `app/services/scoring_service.py` based on the following criteria from README.md:

- Base score: 10 points if `description` is longer than 20 characters
- Briefcase bonus: +5 points if `has_briefcase` is true
- Hopping bonus: +3 points for each instance of "hop" or "hopping" (case-insensitive) in the `description`, up to 15 points
- Twirltastic score: +2 points for every `number_of_twirls`, max 20 points
- Originality factor: +7 points if `walk_name` is unique among submitted applications

### 4. Data Persistence

Store the validated application in the database:

- Generate a UUID for the new application
- Calculate the silliness score using the scoring service
- Set initial status to "PendingReview"
- Add submission timestamp
- Use SQLAlchemy ORM to securely insert the data
- Handle potential database errors securely

### 5. Response Formatting

Return a properly formatted response upon successful creation:

- HTTP status code 201 (Created)
- JSON response including:
  - The generated UUID
  - All submitted application data
  - The calculated silliness score
  - Status ("PendingReview")
  - Submission timestamp

### 6. Error Handling

Implement secure error handling:

- Catch and handle potential exceptions
- Log errors for debugging (without sensitive data)
- Return appropriate HTTP status codes
- Ensure error responses don't reveal implementation details or stack traces

### 7. OpenAPI Documentation

Ensure the endpoint is properly documented in the OpenAPI specification:

- Update FastAPI route decorator with detailed description, summary, and response models
- Include examples in Pydantic models for better API documentation
- Ensure authentication requirements are clearly documented
- Update `docs/api/openapi.yaml` if applicable

## Implementation Guidance

### Secure Coding Best Practices

1. **Input Validation:**
   - Leverage Pydantic's validation capabilities fully
   - Never trust user input
   - Use appropriate field constraints

2. **Authentication:**
   - Implement API key validation before processing the request
   - Use constant-time comparisons for API key validation
   - Return generic error messages for auth failures

3. **Database Operations:**
   - Use SQLAlchemy ORM to prevent SQL injection
   - Implement proper session handling
   - Use transactions where appropriate

4. **Error Handling:**
   - Implement try/except blocks
   - Log detailed errors internally but return generic messages to users
   - Include error codes where helpful without leaking implementation details

### Code Structure

1. **Route Handler:**
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
async def create_application(
    application: ApplicationCreate,
    db: Session = Depends(get_db),
    api_key: str = Depends(get_api_key)
):
    # Implementation details
```

2. **Service Logic:**
   - Move business logic to `application_service.py`
   - Separate concerns between route handlers and business logic
   - Implement scoring in `scoring_service.py`

3. **Documentation:**
   - Add comprehensive docstrings
   - Include examples in Pydantic models
   - Document all possible responses

The implementation should be secure, maintainable, and well-documented, setting a good pattern for future endpoint implementations.
