# Goal and Content of the agent_workflow.md File

## Purpose
The goal of `agent_workflow.md` is to provide a clear, structured process that Copilot Agent should follow when tasked with implementing features or modules for the project. It serves as a "how-to" guide for the AI, ensuring consistent implementation approaches aligned with the project's requirements.

## Intended Content
The file should contain:

1. **A description of the agent's role** - What Copilot Agent is expected to do when implementing tasks

2. **A step-by-step workflow** that includes:
   - Understanding the task and context (reviewing requirements and specifications)
   - Assessment and planning before implementation
   - Rules for adherence to specifications
   - Instructions for handling deviations or ambiguities
   - Code implementation guidelines
   - Quality check procedures
   - **OpenAPI specification update process** (particularly important)
   - Output formatting guidelines
   - Simulated Git commit procedure

3. **Special emphasis on security and documentation** - Particularly for maintaining the OpenAPI specification when API-impacting changes are made

## Example Content Structure
From the copilot-guidance.md, a typical `agent_workflow.md` would include sections like:

```markdown
## Agent Mode - General Implementation Workflow

This document outlines the standard operational procedure for GitHub Copilot Agent when tasked with implementing features or modules for this project.

1. **Understand Task & Context:**
   * Review specific task requirements (from prompt or #file:docs/tasks/YOUR_TASK_FILE.md).
   * Refer to #file:docs/specifications/PROJECT_SPEC.md (architecture, tech stack, MVP goals).
   * Refer to #file:.github/copilot-instructions.md (global conventions, data context).
   * **Crucially, be aware of the OpenAPI specification requirements (#file:README.md Section 8) and Security Robustness requirements (#file:README.md Section 7).**

2. **Assessment & Planning:**
   * Assess existing code for reusability/conflicts. Note dependencies.

3. **Adherence to Specifications:**
   * Implement *only* described features.

4. **Deviation Protocol:**
   * If deviation is strongly beneficial: state proposal, justify, **ask for permission before implementing.**

... (and additional steps as described in the guidance)
```

## Importance
This document is crucial because:
1. It ensures the AI follows a consistent, structured approach
2. It emphasizes key requirements like security and OpenAPI documentation
3. It establishes rules for handling ambiguities or deviations
4. It creates a "standard operating procedure" for all AI-assisted implementations

Once created, this file should be referenced when asking Copilot to implement specific tasks defined in the `docs/tasks/` directory.
