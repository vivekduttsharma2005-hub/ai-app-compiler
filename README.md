# 🤖 AI App Compiler

## Objective

AI App Compiler converts natural language application requirements into structured and executable application configurations.

The project follows a compiler-inspired architecture:

**User Prompt → Intent Extraction → System Design → Schema Generation → Validation → Repair → Runtime Simulation**

---

## Features

### 1. Intent Extraction

Converts user requirements into structured intent JSON.

**Example Input**

```text
Build a CRM with login, contacts, dashboard, role-based access and analytics.
```

**Example Output**

```json
{
  "app_name": "CRM",
  "features": [
    "login",
    "contacts",
    "dashboard",
    "role-based access",
    "analytics"
  ]
}
```

---

### 2. System Design

Automatically generates:

* Entities
* Roles
* Application Architecture

Example:

```json
{
  "entities": [
    "User",
    "Contact",
    "Dashboard",
    "Role",
    "Analytics"
  ],
  "roles": [
    "Admin",
    "Manager",
    "Sales",
    "Marketing"
  ]
}
```

---

### 3. Schema Generation

Generates application configuration including:

* UI Pages
* API Endpoints
* Database Tables

Example:

```json
{
  "ui_pages": [
    "Login",
    "Dashboard"
  ],
  "api_endpoints": [
    "/login",
    "/users"
  ],
  "database_tables": [
    "users",
    "roles"
  ]
}
```

---

### 4. Validation Engine

Detects:

* Invalid JSON
* Missing Keys
* Structural Errors

---

### 5. Repair Engine

Automatically repairs:

* Missing sections
* Missing schema components
* Invalid structures

---

### 6. Runtime Simulator

Simulates execution readiness and reports:

* Generated Pages
* Generated APIs
* Generated Database Tables

---

### 7. Evaluation Framework

Evaluates the system using multiple prompts.

Tracked Metrics:

* Success Rate
* Failure Rate
* Validation Failures
* Repair Count
* Average Latency

---

## Architecture

```text
User Prompt
      │
      ▼
Intent Extraction
      │
      ▼
System Design
      │
      ▼
Schema Generation
      │
      ▼
Validation Engine
      │
      ▼
Repair Engine
      │
      ▼
Runtime Simulation
```

---

## Project Structure

```text
ai-app-compiler/
│
├── app.py
├── app_schema.py
├── intent_extractor.py
├── system_designer.py
├── schema_generator.py
├── validator.py
├── repair_engine.py
├── simulator.py
├── evaluator.py
├── metrics.py
├── assumptions.py
├── test_prompts.json
├── requirements.txt
├── README.md
└── architecture.png
```

---

## Technology Stack

* Python
* Streamlit
* Groq API
* JSON
* Pydantic

---

## Installation

```bash
pip install -r requirements.txt

---

## Run Locally

```bash
streamlit run app.py
```

---

## Example Test Cases

### CRM Application

```text
Build a CRM with login, contacts, dashboard, role-based access and analytics.
```

### E-commerce Platform

```text
Build an ecommerce platform with products, cart, checkout and payments.
```

### Hospital Management System

```text
Build a hospital management system for doctors, patients and appointments.
```

### Edge Case

```text
Build app
```

---

## Deployment

Deploy using Streamlit Cloud.
---

## Cost vs Quality Trade-off

### Model Used

Groq Llama 3.3 70B Versatile

### Advantages

* Fast inference
* Low cost
* Easy deployment
* High-quality structured outputs

### Trade-offs

* Occasional schema inconsistencies
* Ambiguous prompt interpretation

### Mitigation

* Validation Engine
* Repair Engine
* Deterministic Generation
* Runtime Simulation

---

## Future Improvements

* Cross-layer validation
* Dynamic runtime generation
* Real code generation
* Multi-model orchestration
* Automated UI generation
* API implementation generation

---

## Author

**Vivek Dutt Sharma**

AI App Compiler – Internship Project Submission
