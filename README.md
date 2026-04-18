# 🚀 Agentic Coding: From Single Files to Full Systems

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Status](https://img.shields.io/badge/status-experimental-orange)
![License](https://img.shields.io/badge/license-MIT-green)

Generate, run, validate, and test a complete multi-file Python REST API
using an autonomous agent.

------------------------------------------------------------------------

## 🧠 Overview

This project demonstrates an evolution of agentic coding:

    generate → run → validate → test → fix

Instead of generating a single file, the agent builds a **full Clean
Architecture system**.

------------------------------------------------------------------------

## 🧱 Architecture

                 ┌──────────────┐
                 │   Domain     │
                 │  (models)    │
                 └──────┬───────┘
                        │
                 ┌──────▼───────┐
                 │ Application  │
                 │ (services)   │
                 └──────┬───────┘
                        │
                 ┌──────▼───────┐
                 │Infrastructure│
                 │   (SQLite)   │
                 └──────┬───────┘
                        │
                 ┌──────▼───────┐
                 │     API      │
                 │  (FastAPI)   │
                 └──────┬───────┘
                        │
                 ┌──────▼───────┐
                 │    Tests     │
                 │   (pytest)   │
                 └──────────────┘

------------------------------------------------------------------------

## ⚙️ What the Agent Does

-   Generates full multi-file repository
-   Enforces clean architecture
-   Runs API server
-   Installs missing dependencies
-   Executes pytest tests
-   Fixes errors iteratively

------------------------------------------------------------------------

## 🚀 Quick Start

### Clone

    git clone <your-repo-url>
    cd <repo>

### Install dependencies

    pip install openai requests pytest

### Run agent

    python agent_coder_python_clean_arch.py

------------------------------------------------------------------------

## 🧪 Example API Usage

    curl http://localhost:8000/notes

    curl -X POST http://localhost:8000/notes   -H "Content-Type: application/json"   -d '{"content": "hello agent"}'

------------------------------------------------------------------------

## 🧠 Key Concepts

-   Multi-file code generation
-   Architecture-aware agents
-   Test-driven validation
-   Self-healing loops

------------------------------------------------------------------------

## 🔭 Roadmap

-   Multi-file editing (not just generation)
-   Observability (Prometheus + Grafana)
-   Multi-agent orchestration
-   Refactoring agents

------------------------------------------------------------------------

## Related Article

*From Single Files to Full Systems: Agentic Coding for Complete
Repositories*


## Full Project Structure

agentic-clean-architecture/
│
├── agent/                                <-- the agent itself
│   ├── __init__.py
│   ├── main.py                           (entrypoint)
│   ├── generator.py                      (LLM interaction)
│   ├── executor.py                       (run app)
│   ├── tester.py                         (pytest runner)
│   ├── installer.py                      (dependency healing)
│   ├── utils.py                          (helpers)
│   └── config.py                         (GOAL, WORKDIR, etc.)
│
├── project_agent_coded_python_clean_arch/ <-- generated (ignored in git)
│
├── README.md
├── requirements.txt
├── .gitignore
└── agent_coder_python_clean_arch.py 

------------------------------------------------------------------------

## Final Thought

    This is no longer code generation.
    This is autonomous system construction.
