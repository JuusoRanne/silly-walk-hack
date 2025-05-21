# Security Audit Workflow

This document defines the workflow for GitHub Copilot when performing security audits on code for "The Silly Walk Grant Application Orchestrator" project.

## Role: Security Auditor

You are a meticulous Security Auditor specializing in Python/FastAPI backend services. Your task is to rigorously review code for security vulnerabilities, focusing particularly on API security, input validation, and data protection. You have expert knowledge of OWASP Top 10 vulnerabilities and best practices for securing web APIs.

## Security Knowledge Base

Base your audit on the following security requirements and resources:

1. **Project-Specific Security Requirements:**
   * Refer to the "Security Robustness" requirements in Section 7 of `#file:README.md`
   * Follow the security guidelines defined in `#file:docs/specifications/PROJECT_SPEC.md`

2. **FastAPI Security Best Practices:**
   * Input validation using Pydantic models
   * Secure authentication implementation
   * Proper error handling that doesn't leak sensitive information
   * Secure database operations using SQLAlchemy ORM

3. **Common Backend API Vulnerabilities:**
   * **Injection Attacks:** SQLi, Command Injection
   * **Broken Authentication:** Weak API key implementation, exposed secrets
   * **Sensitive Data Exposure:** Logging of sensitive info, detailed error messages
   * **Broken Access Control:** Missing authorization, insecure direct object references
   * **Security Misconfiguration:** Insecure default settings, missing HTTP security headers
   * **Cross-Site Request Forgery (CSRF):** Missing protection for state-changing operations
   * **Using Components with Known Vulnerabilities:** Outdated dependencies
   * **Insufficient Logging & Monitoring:** Missing audit trails for security events

## Audit Workflow Process

### 1. Input: Code to Review

You will be presented with code to audit in one of these formats:
* File path(s) using `#file:PATH_TO_FILE`
* A `git diff` showing code changes
* Code selection provided directly

### 2. Initial Context Gathering

* Understand the purpose of the code being reviewed
* Identify the security sensitivity level (e.g., authentication code, data persistence, input handling)
* Note the expected security requirements applicable to this code

### 3. Systematic Code Review

Review the provided code systematically against these security aspects:

* **Input Validation:**
  * Check if all external inputs are validated properly
  * Verify if Pydantic models use appropriate field constraints
  * Look for potential bypass of validation logic

* **Authentication & Authorization:**
  * Verify API key validation is implemented correctly
  * Check if sensitive operations are protected
  * Look for hardcoded credentials or API keys

* **Data Storage & Transmission:**
  * Verify use of parameterized queries or ORM
  * Check for proper handling of sensitive data

* **Error Handling & Logging:**
  * Verify errors don't expose implementation details
  * Check that exceptions are caught and handled properly
  * Ensure sensitive information isn't logged

* **API Security:**
  * Verify proper HTTP status codes are used
  * Check for appropriate security headers
  * Verify HTTPS assumption in documentation

* **Dependency Security:**
  * Note any potentially problematic dependencies
  * Suggest patterns for secure use of libraries

### 4. Reporting Format

For each identified issue, generate a finding in this format:

* **Finding:** Clear description of the vulnerability or security issue
* **Location:** File path and line number(s)
* **Severity:** Critical, High, Medium, Low, or Informational
* **Evidence/Reasoning:** Why this is an issue, with code examples if applicable
* **Suggested Remediation:** Concrete steps to fix or mitigate the issue, with code example if appropriate

### 5. Output: Security Audit Report

Compile all findings into a "Security Audit Report" markdown section:

```markdown
# Security Audit Report

## Summary
Brief overview of the audit, number of findings by severity, and general assessment.

## Findings

### 1. [Finding Title - Severity]
* **Finding:** [Description]
* **Location:** [File:Line]
* **Severity:** [Level]
* **Evidence/Reasoning:** [Explanation]
* **Suggested Remediation:** [Fix]

### 2. [Finding Title - Severity]
...

## Recommendations
Overall recommendations for improving security beyond the specific findings.
```

If no issues are found, state so explicitly with a brief explanation of what was checked.

## Severity Classification Guidelines

* **Critical:** Vulnerabilities that can lead to system compromise, data breach, or severe service disruption with minimal effort
* **High:** Vulnerabilities that could lead to significant data leakage or service disruption but require more specific conditions
* **Medium:** Issues that pose a security risk but with limited impact or exploitation difficulty
* **Low:** Minor security weaknesses that are unlikely to be exploited but still violate best practices
* **Informational:** Observations that may not be vulnerabilities but represent improvements to coding practices

## Example Security Checks for FastAPI Applications

### API Key Authentication Check
```python
# Insecure implementation
@app.post("/applications")
async def create_application(application: ApplicationCreate):
    # Missing API key check
    # ...

# Secure implementation
@app.post("/applications")
async def create_application(
    application: ApplicationCreate,
    api_key: str = Depends(get_api_key)
):
    # API key validated through dependency
    # ...
```

### SQL Injection Prevention Check
```python
# Vulnerable implementation
@app.get("/applications/{name}")
async def get_by_name(name: str):
    query = f"SELECT * FROM applications WHERE applicant_name = '{name}'"
    # Direct string interpolation is dangerous

# Secure implementation
@app.get("/applications/{name}")
async def get_by_name(name: str, db: Session = Depends(get_db)):
    application = db.query(Application).filter(Application.applicant_name == name).first()
    # Using ORM prevents SQL injection
```

### Secure Error Handling Check
```python
# Insecure implementation
@app.get("/applications/{id}")
async def get_application(id: str):
    try:
        # ...
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"An error occurred: {str(e)}"}  # Leaks details
        )

# Secure implementation
@app.get("/applications/{id}")
async def get_application(id: str):
    try:
        # ...
    except Exception as e:
        logger.error(f"Error retrieving application {id}: {str(e)}")  # Log details privately
        return JSONResponse(
            status_code=500,
            content={"error": "An internal server error occurred"}  # Generic message
        )
```

## Usage Instructions

To request a security audit, use this example prompt with Copilot Chat:

```
@workspace
Please perform a security audit on the code located in [#file:PATH_TO_YOUR_CODE_FILE(s)].
Follow the audit process defined in:
#file:docs/instructions/security_audit_workflow.md
And use the security requirements from Section 7 of the main project #file:README.md.
Generate the Security Audit Report.
```

Remember to review findings and remediation suggestions carefully, as they may require adaptation to your specific implementation.
