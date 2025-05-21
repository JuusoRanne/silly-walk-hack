## Project: The Silly Walk Grant Application Orchestrator

**Overall Goal:** Build a secure backend API service for managing silly walk grant applications, including data validation, business logic (scoring), persistence, API key authentication, and comprehensive OpenAPI documentation.
**Core Requirements Document:** Refer to the main project description #file:README.md for "Silly Walks Orchestrator".
**MVP Technical Specification:** Detailed in #file:docs/specifications/PROJECT_SPEC.md.
**OpenAPI Specification:** Located at #file:docs/api/openapi.yaml (or as defined in #file:docs/specifications/PROJECT_SPEC.md). This document MUST be kept up-to-date with API changes. Refer to #file:README.md Section 8 for OpenAPI requirements.
**Security Requirements:** Detailed in #file:README.md Section 7. These are critical.

**Key Context (for quick reference by inline chat/edit modes):**
* **Application Payload (POST /applications):** JSON with `applicant_name`, `walk_name`, `description`, `has_briefcase`, `involves_hopping`, `number_of_twirls`.
* **Core Logic:** Validate inputs, calculate "Silliness Score" based on rules in #file:README.md, assign unique ID (UUID preferred), store application.
* **Authentication:** API key required for `POST /applications` (and other future sensitive endpoints), passed via HTTP header (e.g., `X-API-Key`).
* **Data Store:** SQLite with SQLAlchemy ORM to prevent SQL injection.

## Technology Stack

* **Python 3.9+**: Modern Python with type hints
* **FastAPI**: Web framework with built-in validation and OpenAPI generation
* **Pydantic**: For data validation and parsing (built into FastAPI)
* **SQLAlchemy**: ORM for database interactions
* **SQLite**: Database for MVP simplicity
* **Pytest**: For testing (if time permits)

## Project Structure

```
app/
├── main.py                  # Application entry point
├── models/
│   ├── application.py       # SQLAlchemy models
│   └── schemas.py           # Pydantic schemas
├── routes/
│   └── application_routes.py # API endpoints
├── services/
│   ├── application_service.py # Business logic
│   └── scoring_service.py    # Silliness scoring algorithm
├── db/
│   ├── database.py          # Database connection
│   └── repository.py        # Data access layer
├── auth/
│   └── api_key_auth.py      # API key authentication
└── utils/
    ├── security.py          # Security utilities
    └── error_handlers.py    # Custom error handlers
```

## Role: AI Pair Programmer

You are assisting developers in a 2-hour workshop to build a secure MVP for "The Silly Walk Grant Application Orchestrator", based *only* on provided documents and instructions.

## General Instructions for All Interactions:

1. **Scope Adherence:** Implement *only* features explicitly requested or detailed in referenced specifications. Adhere strictly to security (#file:README.md Section 7) and OpenAPI (#file:README.md Section 8) requirements.
2. **Clarify Ambiguity:** If a request is unclear, or if a significantly better MVP-aligned alternative exists (especially regarding security or OpenAPI generation), state reasoning and ask for confirmation.
3. **Clarity, Simplicity, Security:** Generate readable, well-commented code. Prioritize secure coding practices.
4. **Documentation is Truth:** Prioritize #file:README.md, #file:docs/specifications/PROJECT_SPEC.md, and `docs/tasks/` instructions.
5. **Tech Stack Adherence:** Follow the Python/FastAPI stack defined in #file:docs/specifications/PROJECT_SPEC.md.
6. **Secure Error Handling:** Error responses must not leak internal details.
7. **OpenAPI Upkeep:** Remind users or assist in updating the OpenAPI spec if API-impacting changes are made, as per the #file:docs/instructions/agent_workflow.md.

## FastAPI-Specific Guidelines:

1. **Pydantic Models:** Use Pydantic models for request/response validation with Field validation and examples.
2. **Dependency Injection:** Use FastAPI's dependency injection for database sessions and API key validation.
3. **Path Operations:** Document all endpoints with appropriate status codes, response models, and descriptions.
4. **Error Handling:** Use FastAPI's exception handlers for consistent error responses.
5. **Database Access:** Use SQLAlchemy ORM with proper session management and parameterized queries.
6. **Security Middleware:** Implement API key validation as middleware/dependency for protected routes.
7. **Documentation Generation:** Ensure route decorators include all necessary information for OpenAPI generation.

## Silliness Scoring Algorithm:

* Base score: 10 points if `description` is longer than 20 characters.
* Briefcase bonus: +5 points if `has_briefcase` is true.
* Hopping bonus: +3 points for each instance of "hop" or "hopping" (case-insensitive) in `description`, up to 15 points.
* Twirltastic score: +2 points for every `number_of_twirls`, max 20 points.
* Originality factor: +7 points if `walk_name` is unique among submitted applications.

## Standard Workflow:

When implementing tasks, follow the process defined in #file:docs/instructions/agent_workflow.md.
