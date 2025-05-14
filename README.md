# Project: The Silly Walk Grant Application Orchestrator

**Mission:** To bring order and cutting-edge (backend) technology, with an unwavering commitment to security and clear documentation, to the esteemed Ministry of Silly Walks' grant application process, ensuring only the silliest (and most securely processed and well-documented) walks receive due consideration!

## 1. Introduction: A Ministry Overwhelmed by Silliness

The Ministry of Silly Walks, a revered public institution, is facing an unprecedented challenge: a deluge of grant applications for new, innovative, and frankly, bewilderingly silly walks. The current manual paper-based system, involving slide rules and tea-leaf readings, is buckling under the strain and, frankly, isn't up to modern security snuff or documentation standards for handling such precious intellectual property.

The Minister has decreed that a new, robust, and highly secure backend system – "The Silly Walk Grant Application Orchestrator" – is required. This system will automate the initial intake, validation, and preliminary "silliness assessment" of grant applications, preparing them for final review by the Grand Council of Gait. Your team's task is to build the MVP of this crucial backend service. There is no need for a user interface; this is a service for internal ministerial use, interacted with via API, and security and comprehensive API documentation are paramount.

## 2. Business Requirements

The Silly Walk Grant Application Orchestrator MVP must fulfill these core backend requirements:

1.  **Application Submission API Endpoint:**
    * The system must expose an API endpoint (e.g., `POST /applications`) that accepts new grant applications.
    * Applications will be submitted as JSON, containing at least:
        * `applicant_name` (string)
        * `walk_name` (string)
        * `description` (string, detailing the walk's silliness)
        * `has_briefcase` (boolean)
        * `involves_hopping` (boolean)
        * `number_of_twirls` (integer)

2.  **Application Validation (Security Focus):**
    * Upon submission, the system must rigorously validate all incoming data against expected types, formats, lengths, and character sets *before* any further processing. This is the first line of defense.
    * Invalid applications should result in an appropriate error response (e.g., HTTP 400 Bad Request) with a clear, but non-revealing, error message.

3.  **Silliness Scoring Algorithm:**
    * The system must implement a "Silliness Score Calculator" based on the following highly scientific criteria (feel free to expand with one or two more of your own devising!):
        * Base score: 10 points if `description` is longer than 20 characters.
        * Briefcase bonus: +5 points if `has_briefcase` is true.
        * Hopping bonus: +3 points for each instance of the word "hop" or "hopping" (case-insensitive) in the `description`, up to a maximum of 15 points from hopping.
        * Twirltastic score: +2 points for every `number_of_twirls`, max 20 points.
        * Originality factor (if `walk_name` is unique among submitted applications so far): +7 points.
    * The calculated silliness score must be associated with the application.

4.  **Application Persistence (Secure Storage):**
    * Validated applications, along with their calculated silliness score and an initial status (e.g., "PendingReview"), must be stored in a persistent data store.
    * For the MVP, this could be a simple in-memory store (understanding data is lost on restart), a local file (JSON, CSV), or a simple database (SQLite). The choice is yours.
    * If using a database, all database interactions *must* use parameterized queries or an Object-Relational Mapper (ORM) to prevent SQL injection vulnerabilities.
    * Each application should receive a unique, non-sequential, and hard-to-guess ID upon storage (e.g., a UUID is preferred over a simple auto-incrementing integer for IDs exposed externally).

5.  **Application Retrieval API Endpoint:**
    * The system must expose an API endpoint (e.g., `GET /applications/{application_id}`) to retrieve a specific application by its unique ID, including its details and silliness score.
    * An endpoint to list all applications (e.g., `GET /applications`) with basic details (ID, walk name, applicant, score, status) would also be beneficial. Consider pagination for this list endpoint.

6.  **Technology Agnosticism:**
    * The choice of backend programming language, framework (if any), and data persistence method is entirely up to the team. Focus on a robust, testable, and secure backend implementation.

7.  **Security Robustness (Utmost Importance):**
    The Ministry handles sensitive (and profoundly silly) intellectual property. Therefore, the system must be designed with security as a top priority from the outset. For the MVP, this means demonstrating understanding and implementation of core security principles:
    * **Input Validation & Sanitization (Reinforced):** As per Requirement #2, all data from external sources (API inputs) must be treated as untrusted. Validate for type, length, format, and range. Sanitize outputs if data is ever echoed back, though this is less critical for a pure backend API not rendering HTML.
    * **Secure API Design & Operation:**
        * **HTTPS by Default:** Design the API with the explicit assumption it will always operate over HTTPS in any deployment.
        * **Secure Error Handling:** API error responses must be generic and not expose internal system details, stack traces, database errors, or other sensitive information that could aid an attacker.
        * **HTTP Headers:** Consider setting security-related HTTP headers (e.g., `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`) even if not directly consumed by non-browser clients, as a best practice.
    * **Authentication & Authorization (Foundational Planning & MVP Requirement):**
        * All data-modifying endpoints (`POST`, `PUT`, `DELETE`, `PATCH`) are considered sensitive.
        * **MVP Requirement:** Implement a simple, secure API key/token-based authentication mechanism. The key should be passed in a standard HTTP header (e.g., `X-API-Key` or `Authorization: Bearer <token>`). The service should validate this key before processing requests to sensitive endpoints. For the workshop, a single, pre-defined (but not obviously guessable) key is acceptable for demonstration, with the understanding that in production this would come from a secure configuration or secrets manager.
    * **Principle of Least Privilege:** If your application involves different internal components or functions, ensure they operate with the minimum permissions necessary for their tasks.
    * **Dependency Security:** Be mindful of third-party libraries. While a full audit is out of scope, choose well-maintained libraries and be aware that dependency scanning is a standard security practice.

8.  **API Documentation (OpenAPI Specification - Mandatory):**
    * The API must be documented using the OpenAPI Specification (version 3.x is recommended).
    * This documentation must accurately describe all implemented API endpoints, including:
        * URL paths and HTTP methods.
        * Request parameters (path, query, header, cookie).
        * Request body schemas (e.g., for the `POST /applications` payload).
        * Response schemas for all possible status codes.
        * Authentication methods applicable to each endpoint (i.e., the API key mechanism).
    * The OpenAPI specification file (e.g., `openapi.yaml` or `openapi.json`) must be committed to the repository (e.g., in a `docs/api/` or root `api/` directory).
    * Teams can create this specification manually, use code annotations with a framework-specific tool/library (if available for their chosen stack), or utilize an OpenAPI editor.

## 3. Core Logic & Data Model (MVP)

* **Application Data Model (Example):**
    * `id`: Unique identifier (UUID recommended)
    * `applicant_name`: String
    * `walk_name`: String
    * `description`: String
    * `has_briefcase`: Boolean
    * `involves_hopping`: Boolean
    * `number_of_twirls`: Integer
    * `silliness_score`: Integer
    * `status`: String (e.g., "PendingReview", "UnderSillyCouncilReview", "ApprovedForFunding", "RegrettablyNotSillyEnough")
    * `submission_timestamp`: DateTime

* **Silliness Scoring:** Implement the rules as defined in Business Requirement #3.

## 4. Expected Outcome & Deliverables

Each team needs to:

1.  Deliver a functional backend service (The Silly Walk Grant Application Orchestrator MVP) meeting all requirements, including the demonstrated security considerations and the **complete OpenAPI documentation file**. API endpoints should be interactable using tools like cURL or Postman, demonstrating API key usage for protected endpoints.
2.  Present a brief (5-10 min) demonstration:
    * Show API interactions: submitting new applications (valid/invalid, with/without API key), retrieving applications.
    * Briefly explain the validation logic, silliness scoring, and implemented security measures (input validation, API key auth, secure error handling).
    * Show how and where application data is persisted.
    * **Show or reference the OpenAPI specification file** that documents the implemented API, explaining how it matches the service.
    * Briefly mention the technology stack chosen.

## 5. Stretch Goals (Optional - If Your Silliness & Security Know No Bounds!)

* **Enhanced Input Validation:** Use dedicated validation libraries for more complex schemas and custom rules.
* **Rate Limiting:** Implement basic rate limiting on API endpoints to prevent abuse.
* **Status Update Endpoint with Authorization:** Add `PUT /applications/{application_id}/status` protected by the API key, allowing status changes.
* **Structured Logging:** Implement logging for requests, errors, and significant events, being careful not to log sensitive data like full API keys.
* **Data-at-Rest Considerations:** If using a database, research and discuss how you would approach encryption for sensitive fields (even if not fully implemented for the MVP).
* **Interactive API Documentation UI:** Set up a tool (e.g., Swagger UI, ReDoc, or a framework-integrated solution) to serve and render your `openapi.yaml`/`openapi.json` file interactively.
* **Automated Security Tests:** Write simple tests that specifically try to submit malicious or malformed input to check validation robustness.

## 6. How to Get Started (Workshop Instructions)

1.  Clone this repository (or start a new one for this project).
2.  Design your API endpoints and data structures. **Concurrently, start drafting your OpenAPI specification (`openapi.yaml` or `openapi.json`)** to define these contracts formally. This can be an iterative process.
3.  Implement the application submission, validation (with security focus), scoring, persistence (using secure practices), and retrieval logic. Implement the API key authentication.
4.  **Continuously update your OpenAPI specification** as you implement and refine your API endpoints.
5.  Test your API endpoints thoroughly, including security aspects. Use your OpenAPI document as a reference for testing.
6.  Commit your code and OpenAPI specification file regularly. Prepare for your demonstration!