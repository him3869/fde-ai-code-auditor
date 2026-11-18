# FDE AI Code Auditor

An AI-powered static analysis and code review web application built with **FastAPI**, **Google Gemini**, and **Docker**. Designed using a **Backend-for-Frontend (BFF)** architecture to keep LLM credentials isolated server-side while delivering real-time, structured security and quality audits.

**Live Demo:** [https://fde-ai-code-auditor.onrender.com/](https://fde-ai-code-auditor.onrender.com/)  
*(Note: Hosted on Render's free tier—initial page load may take 30–60 seconds if the container is waking from sleep.)*

---

## Architecture Overview

Rather than exposing API keys in a client-side static app, this project implements a stateless **Backend-for-Frontend (BFF)** pattern:

    Browser (index.html)  ──[ HTTPS / JSON ]──>  FastAPI Server (Docker)  ──[ google-genai ]──>  Google Gemini API
    Tailwind CSS Dark UI  <──[ Structured   ]──  Prompt + System Rules    <──[ Security Audit ]──  LLM Analysis

### Key Engineering Decisions
- **Credential Isolation:** The `GEMINI_API_KEY` is injected exclusively at runtime via environment variables inside the container and never touches the browser.
- **Decoupled Prompt Engineering:** System auditing guidelines (`review_instructions.txt`) are separated from application routing logic (`main.py`), allowing rapid iteration on audit criteria without modifying API endpoints.
- **Portable Containerization:** Packaged with a lightweight `Dockerfile` to ensure identical execution across local Apple Silicon development environments and cloud Linux instances.

---

## Tech Stack

- **Backend:** Python, FastAPI, Uvicorn
- **AI / LLM Integration:** Google GenAI SDK (`google-genai`)
- **Frontend:** HTML5, Vanilla JavaScript, Tailwind CSS
- **Infrastructure & DevOps:** Docker, GitHub, Render (CI/CD auto-deploy from `main`)

---

## Project Structure

    fde-ai-code-auditor/
    ├── Dockerfile               # Container definition for cloud & local deployment
    ├── main.py                  # FastAPI application, endpoints, and Gemini SDK integration
    ├── index.html               # Responsive dark-mode frontend interface
    ├── review_instructions.txt  # System prompt & auditing rubric for Gemini
    ├── requirements.txt         # Pinned Python dependencies
    └── .gitignore               # Excludes environment files and Python bytecode

---

## Running Locally with Docker

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- A valid [Google Gemini API Key](https://aistudio.google.com/)

### 1. Clone the Repository
    git clone https://github.com/him3869/fde-ai-code-auditor.git
    cd fde-ai-code-auditor

### 2. Build the Docker Image
    docker build -t fde-code-agent .

### 3. Run the Container
    docker run -d -p 8000:8000 -e GEMINI_API_KEY="your_api_key_here" --name fde-running-app fde-code-agent

Open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your browser to use the auditor locally.

---

## Local Development (Without Docker)

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    export GEMINI_API_KEY="your_api_key_here"
    uvicorn main:app --reload

---

## Future Improvements
- **Structured JSON Schema Enforcement:** Enforce strict Pydantic response schemas for deterministic severity tagging (`Critical`, `Warning`, `Info`) and automated patch diffs.
- **GitHub PR Webhook Integration:** Extend the FastAPI backend to listen for pull request events and post automated inline review comments.
- **Rate Limiting & Telemetry:** Add request throttling and token usage logging for production observability.
