# AI App Compiler

## Objective

AI App Compiler converts natural language application requirements into structured and executable application configurations.

The project follows a compiler-inspired architecture:

User Prompt
→ Intent Extraction
→ System Design
→ Schema Generation
→ Validation
→ Repair
→ Runtime Simulation

---

## Features

### Intent Extraction

Converts user requirements into structured intent.

### System Design

Generates:

- Entities
- Roles

### Schema Generation

Generates:

- UI Schema
- API Schema
- Database Schema

### Validation Engine

Checks:

- Invalid JSON
- Missing Keys
- Structural Errors

### Repair Engine

Automatically repairs:

- Missing sections
- Missing schema components

### Runtime Simulator

Validates execution readiness.

### Evaluation Framework

20 Prompt Dataset

Metrics:

- Success Rate
- Failure Rate
- Validation Failures
- Repairs
- Average Latency

---

## Project Structure

ai-app-compiler/
├── app.py
├── pipeline/
├── runtime/
├── evaluation/
├── schemas/

---

## Technology Stack

- Python
- Streamlit
- Groq API
- Pydantic

---

## Run Locally

pip install -r requirements.txt

streamlit run app.py

---

## Deployment

Deploy on Streamlit Cloud.

---

## Cost vs Quality Tradeoff

Model: Groq Llama 3

Advantages:

- Fast
- Cheap
- Easy Deployment

Tradeoffs:

- Occasional schema inconsistencies

Mitigation:

- Validation Engine
- Repair Engine
- Deterministic Generation

---

## Evaluation Metrics

The system tracks:

- Success Rate
- Failure Rate
- Validation Errors
- Repair Count
- Average Latency

---

## Future Improvements

- Cross-layer validation
- Dynamic runtime generation
- Real code generation
- Multi-model orchestration
