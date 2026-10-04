# Pantry Search Demo

A small Python + SQLite repository for demonstrating a reproduce-first GitHub Copilot workflow.

## Setup

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
pytest -q
ruff check .
bandit -r app -q
```

The `main` starting state intentionally contains a SQL injection weakness for a controlled demo. Use synthetic data only.
