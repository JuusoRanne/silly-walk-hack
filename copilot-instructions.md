# GitHub Copilot Workshop Guide

## 1. Introduction (Approx. 5 minutes)

This guide outlines how to use GitHub Copilot effectively for "The Silly Walk Grant Application Orchestrator" project (a backend-focused service). The aim is to use Copilot for planning, documentation-driven development, secure implementation, and API documentation within a timed workshop (e.g., 2 hours). The focus is on structured collaboration with AI.

## 2. Phase 1: Ideation & Planning with Copilot (Approx. 30-40 minutes)

This phase is crucial for setting a clear direction. Effective planning and documentation here will significantly streamline the implementation phase with Copilot.

### 2.1. Review Project Requirements
Refer to the main project description document (e.g., `README.md`) for "The Silly Walk Grant Application Orchestrator" to understand the project's goals, business requirements (including security and OpenAPI mandates). Ensure every team member has a clear grasp of the MVP.

### 2.2. Planning Approach with Copilot
Use Copilot Chat for this phase to brainstorm and refine your project's direction.
* **Option A (AI-Led Brainstorming):** If your team is unsure where to start.
    * **Example Prompt (Copilot Chat):**
        ```
        Review the main project description document (e.g., `README.md`) for 'The Silly Walk Grant Application Orchestrator'. This project involves building a secure backend API with data validation, business logic (scoring), data persistence, API key authentication, and mandatory OpenAPI documentation.
        1. Propose 2 distinct application architectures (e.g., a RESTful API service using a specific backend framework, a microservice-oriented approach for distinct functions like submission and scoring).
        2. For each architecture, suggest suitable primary programming languages (e.g., Node.js/Express, Python/FastAPI, Java/Spring Boot) and relevant key frameworks/libraries for API development, data persistence (e.g., ORMs like Sequelize/SQLAlchemy, or direct DB drivers), security aspects, and OpenAPI generation.
        3. Outline main components for each (e.g., API route handlers, validation service, scoring engine, data access layer).
        Focus on an MVP achievable in 2 hours that meets all core requirements.
        ```
* **Option B (Participant-Led, AI-Refined):** If your team has initial ideas.
    * **Example Prompt (Copilot Chat):**
        ```
        For 'The Silly Walk Grant Application Orchestrator' project (described in the main project `README.md`), we plan a [describe your architecture, e.g., 'Node.js Express application using Sequelize for SQLite persistence, with API key authentication and generating OpenAPI docs using swagger-jsdoc'].
        1. Is this MVP (including security basics and OpenAPI spec) feasible in 2 hours?
        2. Suggest key libraries/modules for our chosen stack that would be good for request validation, implementing the scoring logic, secure API key handling, and generating the OpenAPI spec from code comments?
        3. Outline the main functional modules (e.g., route files, controller/service files, models).
        ```

### 2.3. Define Architecture & Tech Stack
Based on the brainstorming, your team should decide on:
* The high-level architecture.
* The primary programming language(s) and key frameworks/libraries for the backend service, including for API documentation.
Documenting these choices is the next step.

### 2.4. Create Project Specification Documentation
Clear specifications are vital for guiding both your team and Copilot. These documents should be created collaboratively and iteratively.

**Workflow for Creating Specification Documents:**
It's recommended to create these specification files (`ARCHITECTURE.md`, `BACKLOG.md`, `PROJECT_SPEC.md`) individually.
1.  Discuss the content for each section/file as a team.
2.  Use Copilot Chat, particularly with **Copilot Edits** (e.g., using `#file` or `#selection` in Copilot Chat to target specific files/parts of files), to help draft, update, and refine each document.
3.  Manually create the `docs/specifications/` folder and the empty markdown files first. This makes it easier for Copilot Edits to target them.

**Key Specification Files:**

* **1. Architecture Diagram (`docs/specifications/ARCHITECTURE.md`):**
    * **Purpose:** Visually represent your chosen application architecture.
    * **Content:** Use text-based diagramming tools like Mermaid JS, PlantUML, or a clear textual outline of components (e.g., API Gateway/Router, Controllers/Services, Data Access Layer, Database).
    * **Example Prompt (Copilot Chat with Edits for `ARCHITECTURE.md`):**
        ```
        #file docs/specifications/ARCHITECTURE.md
        Based on our decision to build a [e.g., 'RESTful API using {Your Chosen Framework} for The Silly Walk Grant Application Orchestrator'], help me draft a Mermaid JS component diagram illustrating the main backend components (e.g., API Endpoints, Validation Service, Scoring Engine, Persistence Service) and their interactions.
        ```

* **2. Feature Backlog (`docs/specifications/BACKLOG.md`):**
    * **Purpose:** List the features required for the MVP, broken down into manageable tasks.
    * **Content:** A list of features/user stories. Prioritize for the MVP.
    * **Example Prompt (Copilot Chat with Edits for `BACKLOG.md`):**
        ```
        #file docs/specifications/BACKLOG.md
        Based on 'The Silly Walk Grant Application Orchestrator' MVP requirements (see README.md), help me create a feature backlog. Key MVP tasks include:
        - Define API contract and create initial OpenAPI specification file (e.g., docs/api/openapi.yaml).
        - Implement POST /applications endpoint.
        - Implement input validation for application submission.
        - Implement API key authentication for the POST endpoint.
        - Develop Silliness Scoring Algorithm logic.
        - Implement data persistence for applications (e.g., using an in-memory store or SQLite).
        - Implement GET /applications/{id} endpoint.
        - Implement GET /applications (list) endpoint.
        - Ensure OpenAPI specification is updated to reflect all implemented endpoints and schemas.
        Break these down into clear backlog items.
        ```

* **3. Main Project Specification (`docs/specifications/PROJECT_SPEC.md`):**
    * **Purpose:** A central document summarizing key decisions and linking to other detailed specifications.
    * **Location:** `docs/specifications/PROJECT_SPEC.md`
    * **Content Outline:**
        * Project Goal (briefly, from the main `README.md` for Silly Walks Orchestrator)
        * Reference to Architecture Diagram: "See `docs/specifications/ARCHITECTURE.md`"
        * Reference to Feature Backlog: "See `docs/specifications/BACKLOG.md`"
        * Chosen Technology Stack (specific languages, frameworks, database, OpenAPI tools)
        * Key Modules/Components & Their Primary Responsibilities (high-level textual description)
        * Location of OpenAPI specification file (e.g., `docs/api/openapi.yaml`).
    * **Example Prompt (Copilot Chat with Edits for `PROJECT_SPEC.md`, after drafting ARCHITECTURE and BACKLOG):**
        ```
        #file docs/specifications/PROJECT_SPEC.md
        Help me create the main project specification for 'The Silly Walk Grant Application Orchestrator'.
        It should include:
        - Project Goal (summary, emphasizing secure backend API and OpenAPI).
        - Reference to `docs/specifications/ARCHITECTURE.md`.
        - Reference to `docs/specifications/BACKLOG.md`.
        - Our chosen Technology Stack: [e.g., Python/FastAPI, SQLAlchemy for ORM with SQLite, Pydantic for validation, FastAPI's built-in OpenAPI generation].
        - Brief outline of Key Modules/Components: [e.g., `main.py` (API routes), `services/scoring_service.py`, `db/models.py`, `auth/api_key_auth.py`].
        - Path to OpenAPI file: `docs/api/openapi.json`.
        ```

---

## 3. Phase 2: Setup for Copilot-Driven Implementation (Approx. 20-25 minutes)

With a plan in place, configure your environment and key instruction files.

### 3.1. Version Control with Git
Initialize Git and commit frequently: `git init`, `git add .`, `git commit -m "Initial planning and specification documents created"`.

### 3.2. Global Copilot Instructions (`.github/copilot-instructions.md`)
This file provides project-wide, persistent context to Copilot in VS Code.
* **Location:** `.github/copilot-instructions.md`
* **Example Content:**
    ```markdown
    ## Project: The Silly Walk Grant Application Orchestrator

    **Overall Goal:** Build a secure backend API service for managing silly walk grant applications, including data validation, business logic (scoring), persistence, API key authentication, and comprehensive OpenAPI documentation.
    **Core Requirements Document:** Refer to the main project description `README.md` for "Silly Walks Orchestrator".
    **MVP Technical Specification:** Detailed in `docs/specifications/PROJECT_SPEC.md`.
    **OpenAPI Specification:** Located at `docs/api/openapi.yaml` (or as defined in `PROJECT_SPEC.md`). This document MUST be kept up-to-date with API changes. Refer to `README.md` Section 8 for OpenAPI requirements.
    **Security Requirements:** Detailed in `README.md` Section 7. These are critical.

    **Key Context (for quick reference by inline chat/edit modes):**
    * **Application Payload (POST /applications):** JSON with `applicant_name`, `walk_name`, `description`, `has_briefcase`, `involves_hopping`, `number_of_twirls`.
    * **Core Logic:** Validate inputs, calculate "Silliness Score" based on rules in `README.md`, assign unique ID (UUID preferred), store application.
    * **Authentication:** API key required for `POST /applications` (and other future sensitive endpoints), passed via HTTP header (e.g., `X-API-Key`).
    * **Data Store:** Team's choice (MVP can be in-memory, file, or SQLite), using parameterized queries/ORM if SQL.

    ## Role: AI Pair Programmer

    You are assisting developers in a 2-hour workshop to build a secure MVP for "The Silly Walk Grant Application Orchestrator", based *only* on provided documents and instructions.

    ## General Instructions for All Interactions:

    1.  **Scope Adherence:** Implement *only* features explicitly requested or detailed in referenced specifications. Adhere strictly to security (README Section 7) and OpenAPI (README Section 8) requirements.
    2.  **Clarify Ambiguity:** If a request is unclear, or if a significantly better MVP-aligned alternative exists (especially regarding security or OpenAPI generation), state reasoning and ask for confirmation.
    3.  **Clarity, Simplicity, Security:** Generate readable, well-commented code. Prioritize secure coding practices.
    4.  **Documentation is Truth:** Prioritize `README.md`, `PROJECT_SPEC.md`, and `docs/tasks/` instructions.
    5.  **Tech Stack Adherence:** Follow choices in `docs/specifications/PROJECT_SPEC.md`.
    6.  **Secure Error Handling:** Error responses must not leak internal details.
    7.  **OpenAPI Upkeep:** Remind users or assist in updating the OpenAPI spec (`docs/api/openapi.yaml`) if API-impacting changes are made, as per the `agent_workflow.md`.
    ```

### 3.3. Guiding Documents for Copilot Agent Mode & Complex Tasks

You'll use two main types of instruction documents:

1.  **Generic Agent Workflow (`docs/instructions/agent_workflow.md`):** This defines *how* Copilot Agent should generally operate for any task. **Crucially, this workflow will now include a step for updating OpenAPI documentation.**

2.  **Specific Task Documents (e.g., `docs/tasks/TASK_NAME.md`):** For each backlog item, detailing *what* to build for that task, referencing the generic workflow.

**Example 1: Generic Agent Workflow File (with OpenAPI update step)**
* **Location:** `docs/instructions/agent_workflow.md`
* **Content:**
    ```markdown
    ## Agent Mode - General Implementation Workflow

    This document outlines the standard operational procedure for GitHub Copilot Agent when tasked with implementing features or modules for this project.

    1.  **Understand Task & Context:**
        * Review specific task requirements (from prompt or `docs/tasks/` file).
        * Refer to `docs/specifications/PROJECT_SPEC.md` (architecture, tech stack, MVP goals).
        * Refer to `.github/copilot-instructions.md` (global conventions, data context).
        * **Crucially, be aware of the OpenAPI specification requirements (README.md Section 8) and Security Robustness requirements (README.md Section 7).**
    2.  **Assessment & Planning:**
        * Assess existing code for reusability/conflicts. Note dependencies.
    3.  **Adherence to Specifications:** Implement *only* described features.
    4.  **Deviation Protocol:** If deviation is strongly beneficial: state proposal, justify, **ask for permission before implementing.**
    5.  **Code Implementation:** Write clear, concise, well-commented, secure code per task requirements and style guides.
    6.  **Post-Implementation Quality Checks (Simulated for Workshop):**
        * **(Linting):** Assume code is linted/formatted. Aim for passing code.
        * **(Testing):** Assume unit tests are run. Aim for passing code.
        * **(Fixes):** Attempt to fix simulated errors.
    7.  **OpenAPI Specification Update:**
        * Analyze the changes implemented in this task (e.g., by reviewing a conceptual `git diff` of modified code files relevant to API definitions).
        * If any API endpoints (routes, request/response schemas, parameters, authentication methods) were added, modified, or removed:
            * Update the project's OpenAPI specification file (e.g., `docs/api/openapi.yaml` or as defined in `PROJECT_SPEC.md`).
            * Ensure the OpenAPI documentation accurately reflects the current state of the API, adhering to the guidelines in the project `README.md` (Section 8).
            * If tools are used to auto-generate the OpenAPI spec from code (e.g., from annotations), state that these tools would be run or annotations must be updated.
    8.  **Output:** Provide complete code for module(s)/functions. Indicate changes to existing files. State if OpenAPI spec was (or would need to be) updated.
    9.  **Git Commit (Simulated for Workshop):**
        * Indicate a simulated commit message (e.g., "feat: Implement /applications POST endpoint and update OpenAPI spec"). Max 160 chars.
    ```

**Example 2: Specific Task Document for Silly Walks Orchestrator**
* **Location (example):** `docs/tasks/IMPLEMENT_POST_APPLICATIONS_ENDPOINT.md`
* **Content:**
    ```markdown
    ## Task: Implement POST /applications Endpoint

    **Workflow Reference:** When implementing this task, adhere to the general procedure outlined in `docs/instructions/agent_workflow.md`. **Pay special attention to the OpenAPI Specification Update step.**

    **Project Specification Reference:** `docs/specifications/PROJECT_SPEC.md`
    **README.md References:** Section 2 (Business Requirements, esp. #1, #2, #7), Section 8 (OpenAPI).
    **Target Module(s):** [e.g., `src/routes/application_routes.js` and `src/controllers/application_controller.js`, or equivalent for chosen stack]
    **Assigned Role:** Backend API Developer with a focus on security and documentation.
    **Goal:** Implement the `POST /applications` endpoint to allow submission of new silly walk grant applications, including input validation, API key authentication, silliness scoring, data persistence, and ensuring the OpenAPI spec is updated.

    ---
    **Specific Requirements & Acceptance Criteria for this Task:**

    1.  **Endpoint Definition:** Create a `POST` endpoint at `/applications`.
    2.  **API Key Authentication:** Implement API key check (from HTTP header) as per `README.md` Section 7. Reject if invalid/missing.
    3.  **Input Validation:** Rigorously validate the JSON request body against `README.md` Requirement #1 (fields: `applicant_name`, `walk_name`, etc.) and Requirement #2 (security focus on validation). Return HTTP 400 for invalid data.
    4.  **Silliness Scoring:** If validation passes, calculate the silliness score using the logic from `README.md` Requirement #3.
    5.  **Data Persistence:** Store the validated application data, generated UUID, calculated score, initial status ("PendingReview"), and submission timestamp. Use parameterized queries/ORM if SQL.
    6.  **Response:** On successful creation (HTTP 201), return the created application object including its new ID and silliness score. On error, return appropriate HTTP status and non-revealing error message.
    7.  **OpenAPI Documentation:** Ensure this new endpoint, its request body, responses (success and error), and security requirements (API key) are accurately documented in the project's OpenAPI specification file (e.g., `docs/api/openapi.yaml`).
    8.  **Security:** Adhere to all relevant security principles from `README.md` Section 7.
    ```

### 3.4. Building Your Security Audit Agent Workflow (Team Task - Approx. 10 minutes of this Phase)

Before diving deep into feature implementation, your team will define a workflow for a "Security Audit Agent." This involves creating an instruction file that will guide Copilot to act as a security auditor for your code.

* **Create the File:** `docs/instructions/security_audit_workflow.md`
* **Objective:** This document will tell Copilot how to review code changes or existing code for security vulnerabilities.
* **Guidance for Content (Use Copilot Chat to help you draft this!):**
    * **Role:** Define the role for Copilot (e.g., "You are a meticulous Security Auditor...").
    * **Knowledge Base:** Instruct the agent to base its audit on:
        * The "Security Robustness" requirements (Section 7) in the project's `README.md`.
        * **Brainstorm with Copilot:** Ask Copilot Chat: "What are common backend API security vulnerabilities for a project like 'The Silly Walk Grant Application Orchestrator' using [your chosen tech stack, e.g., Node.js/Express]? List 3-5 additional checks beyond what's in our README." Incorporate these into the auditor's knowledge base. (Examples: Insecure Direct Object References, Mass Assignment, Sensitive Data Exposure in logs/responses, outdated dependencies - though deep dependency check is out of scope for runtime audit).
    * **Workflow for the Auditor Agent:**
        1.  Input: Specify that the agent will be given code (e.g., a `git diff`, file path(s), or code selection).
        2.  Review Process: Go through the provided code.
        3.  Assessment: Compare the code against the defined security criteria (from `README.md` and the brainstormed list).
        4.  Reporting Format: For each identified potential issue, generate a report item with a fixed format:
            * `Finding:` (Clear description of the potential vulnerability).
            * `Location:` (File path and line number(s) if applicable).
            * `Severity:` (Assign a level: e.g., Critical, High, Medium, Low, Informational).
            * `Evidence/Reasoning:` (Why this is a potential issue).
            * `Suggested Remediation:` (Concrete steps to fix or mitigate the issue).
        5.  Output: Compile all findings into a "Security Audit Report" markdown section. If no issues are found, state that.
* **Your Task:** Collaboratively draft the content for `docs/instructions/security_audit_workflow.md` using these guidelines.

---

## 4. Phase 3: Iterative Implementation with Copilot (Approx. 40-50 minutes)

Now, translate your plans and specifications into code.

### 4.1. Implement Bare Bones
Use Copilot Chat to kick off implementation, referencing your documentation.
* **Example Prompt (Copilot Chat, guiding Copilot Agent mode or a comprehensive chat interaction):**
    ```
    @workspace
    I need you to implement the `POST /applications` endpoint for 'The Silly Walk Grant Application Orchestrator'.

    **Task Specification:** The detailed requirements are in:
    `docs/tasks/IMPLEMENT_POST_APPLICATIONS_ENDPOINT.md`

    **Implementation Workflow:** The general instructions on how you should approach implementation are in:
    `docs/instructions/agent_workflow.md`

    Please proceed with the full task as described in `docs/tasks/IMPLEMENT_POST_APPLICATIONS_ENDPOINT.md`, ensuring you follow the workflow in `docs/instructions/agent_workflow.md`, especially the OpenAPI update step.
    ```

### 4.2. Work Through Backlog & Conduct Security Audits
Address items from `docs/specifications/BACKLOG.md`. For each significant feature:
1.  Create a new specific task document in `docs/tasks/`.
2.  Reference `docs/instructions/agent_workflow.md`. Detail task-specific requirements.
3.  Use Copilot Chat/Agent mode with your task document.
4.  **After implementing and basic testing:** Use your `security_audit_workflow.md` to audit the new/changed code.
    * **Example Audit Prompt (Copilot Chat):**
        ```
        @workspace
        Please perform a security audit on the code recently implemented for the [feature name, e.g., 'application submission endpoint'] located in [file path(s), e.g., `src/routes/application_routes.js`].
        Follow the audit process defined in:
        `docs/instructions/security_audit_workflow.md`
        And use the security requirements from Section 7 of the main project `README.md`.
        Generate the Security Audit Report.
        ```
5.  Review the audit report and discuss any findings with Copilot for remediation ideas if needed.

### 4.3. Code Testing
Verify functionality and security.
* **Example Prompt (Copilot Chat for writing API tests):**
    ```
    @workspace
    For the `POST /applications` endpoint (defined in `docs/api/openapi.yaml` and implemented in [your relevant file]), help me write integration tests using [your chosen testing framework, e.g., Jest with Supertest for Node.js, or Pytest for FastAPI].
    Tests should cover:
    1. Successful application submission with a valid API key and data. (Expected: 201 Created)
    2. Attempted submission with an invalid/missing API key. (Expected: 401 Unauthorized or 403 Forbidden)
    3. Attempted submission with invalid input data (e.g., missing required field). (Expected: 400 Bad Request)
    ```

### 4.4. Review, Refactor, Commit Loop
Critically review, refactor for clarity/security/performance, and commit working changes frequently.

## 5. Phase 4: Wrap-up & Presentation Prep (Approx. 15 minutes)

* Finalize MVP features as per your `BACKLOG.md`.
* Ensure the API is runnable and OpenAPI spec is up-to-date.
* Prepare a brief demo, including showing the OpenAPI doc and mentioning the security audit process.

## 6. Key Takeaways: AI Collaboration Workflow (Approx. 5 minutes)

* **Documentation as Code for AI:** Structured documents (`PROJECT_SPEC.md`, `agent_workflow.md`, task files, `copilot-instructions.md`) are essential for effectively guiding advanced AI capabilities.
* **Security First Mindset:** Integrating security considerations (and even automated audit prompts) from the start is crucial for backend development.
* **API Documentation is Key:** Keeping OpenAPI (or similar) specifications accurate and up-to-date is a vital backend discipline. Automating parts of this with AI is a valuable skill.
* **Iterative Development:** Plan, instruct AI, implement, test, audit, review, refactor, and commit is a powerful loop.