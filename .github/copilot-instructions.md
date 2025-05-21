## Project: The Silly Walk Grant Application Orchestrator

**Purpose:**  
This backend service securely stores silly walk grant applications and calculates their "silliness" score. The backend is implemented in Python. All code must be reusable, modular, and follow best security practices.

---

### Coding Conventions

- **Language:** Python (latest stable 3.x)
- **Variable Naming:** Use `snake_case` (underscores as word separators). Variable and function names must clearly reflect their purpose (e.g., `calculate_silliness_score`, `validate_application_input`).
- **Reusability:**  
  - Structure code into reusable modules and functions (e.g., separate validation, scoring, persistence, and API logic).
  - Avoid duplication; use helper functions/classes where appropriate.
- **Security:**  
  - Validate all external input for type, length, format, and allowed values before processing.
  - Use parameterized queries or ORM for all database access.
  - Do not expose internal errors or stack traces in API responses.
  - Implement API key authentication for all data-modifying endpoints.
- **Documentation:**  
  - All API endpoints must be documented in OpenAPI (YAML or JSON).
  - Add docstrings to all public functions and classes.
- **Testing:**  
  - Write reusable test functions for validation, scoring, and API endpoints.

---

### Key Features

- **Endpoints:**  
  - `POST /applications`: Accepts new silly walk applications (JSON).
  - `GET /applications/{application_id}`: Retrieves a specific application.
  - `GET /applications`: Lists all applications (consider pagination).
- **Core Logic:**  
  - Validate application input strictly.
  - Calculate silliness score using the rules in [README.md](README.md).
  - Store applications with a UUID, score, and status.
- **Persistence:**  
  - Use in-memory, file-based, or SQLite storage (with ORM or parameterized queries).
- **Authentication:**  
  - Require API key in a standard HTTP header for sensitive endpoints.

---

### Copilot Guidance

- Always use variable and function names that clearly describe their intent and use `snake_case`.
- Prefer modular, reusable code—split logic into functions and classes where possible.
- Follow the security and validation requirements from [README.md](README.md) Section 7.
- Ensure all API changes are reflected in the OpenAPI spec.
- Do not implement features outside the described requirements unless explicitly asked.

---