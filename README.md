# FDE AI Code Auditor

An AI-powered static analysis and code review web application built with **FastAPI**, **Google Gemini**, and **Docker**. Designed using a **Backend-for-Frontend (BFF)** architecture to keep LLM credentials isolated server-side while delivering real-time, structured security and quality audits.

**Live Demo:** [https://fde-ai-code-auditor.onrender.com/](https://fde-ai-code-auditor.onrender.com/)  
*(Note: Hosted on Render's free tier—initial page load may take 30–60 seconds if the container is waking from sleep.)*

---

## Architecture Overview

Rather than exposing API keys in a client-side static app, this project implements a stateless **Backend-for-Frontend (BFF)** pattern:

```text
┌─────────────────────────┐       HTTPS / JSON       ┌──────────────────────────┐       google-genai       ┌─────────────────────┐
│   Browser (index.html)  │ ───────────────────────► │  FastAPI Server (Docker) │ ───────────────────────► │  Google Gemini API  │
│  Tailwind CSS Dark UI   │ ◄─────────────────────── │  Prompt + System Rules   │ ◄─────────────────────── │   Structured Audit  │
└─────────────────────────┘                          └──────────────────────────┘                          └─────────────────────┘

