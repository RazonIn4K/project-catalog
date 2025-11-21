# Requirements: TaskFlow Pro SaaS Backend

## 1. Overview

TaskFlow Pro is a project management SaaS. This backend provides the core API for task management, user authentication, and an AI-powered "Subtask Generator" feature.

## 2. Functional Requirements

### 2.1. Authentication

- **REQ-AUTH-01:** The system SHALL support JWT-based authentication.
- **REQ-AUTH-02:** Users SHALL be able to register and login.

### 2.2. Task Management

- **REQ-TASK-01:** Users SHALL be able to CRUD (Create, Read, Update, Delete) tasks.
- **REQ-TASK-02:** Tasks SHALL have a status (Todo, In Progress, Done) and priority.

### 2.3. AI Features

- **REQ-AI-01:** The system SHALL provide an endpoint `POST /tasks/{id}/suggest-subtasks`.
- **REQ-AI-02:** This endpoint SHALL use an LLM to break down a complex task into 3-5 actionable subtasks.

## 3. Non-Functional Requirements

- **REQ-PERF-01:** API response time SHALL be under 200ms for non-AI endpoints.
- **REQ-DOC-01:** The API SHALL be documented using OpenAPI/Swagger.
