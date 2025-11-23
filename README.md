# 📦 TO dO list Project

A backend system for managing **projects** and **tasks**, built with **FastAPI** and a **deprecated CLI** for transitional use.  
Includes background scheduling for periodic jobs (e.g., auto‑closing overdue tasks).

---

## 🚀 Features
- **FastAPI Web API** with modular structure:
  - Controllers (`api/controllers`)
  - Routers (`api/routers.py`)
  - Request/Response Schemas (`api/controller_schemas`)
- **CRUD operations** for Projects and Tasks
- **PATCH endpoints** for partial updates
- **GET by name** endpoints for quick lookups
- **Background scheduler** for periodic jobs
- **CLI (deprecated)** still available for backward compatibility

---

## 📂 Project Structure
app/
├── api/
|  ├── controllers/
|  | ├── __init__.py
|  │ ├── projects_controller.py
|  │ └── tasks_controller.py
|  ├── controller_schemas/
|  │ ├── requests/
|  │ │ ├── projects_request_schema.py
|  │ │ └── tasks_request_schema.py
|  │ └── responses/
|  │   ├── projects_response_schema.py
|  │   └── tasks_response_schema.py
|  ├── __init__.py
|  └── routers.py
├── exceptions/
│ ├── __init__.py
│ ├── base.py
│ ├── repository_exceptions.py
│ └── service_exceptions.py
│
├── models/
│ ├── __init__.py
│ ├── project.py
│ └── task.py
│
├── repositories/
│ ├── __init__.py
│ ├── project_repository.py
│ └── task_repository.py
│
├── services/
│ ├── __init__.py
│ ├── project_service.py
│ └── task_service.py
│
├── commands/
│ ├── __init__.py
│ ├── autoclose_overdue.py
│ └── scheduler.py 
│
├── cli/
│ ├── __init__.py
│ └── console.py # Deprecated CLI
│
├── db/
│ ├── __init__.py
│ ├── base.py
│ └── session.py # SQLAlchemy session + get_db
│
└── main.py # Unified entrypoint (CLI + API)
alembic/
└── ... (revisions and env.py)
.env
.env.example
pyproject.toml
poetry.lock
.gitignore

---

## ⚙️ Setup

### 1. Clone & Install dependencies
```bash
git clone https://github.com/KasraMousapour/ToDoList.git

```
install packages from pyproject.toml file based on poetry. 

### 2. Configure Database 
Set your database URL and limits in environment variables based on .env.example file

### 3. Run Migrations
(assuming Alembic is configured)
```bash
alembic upgrade head

```
--- 

## 🖥️ Running the Application

### Run FastAPI (default mode)
```bash
poetry run python main.py --mode api 

```

### Run FastAPI with reload (development)
```bash
poetry run python main.py --mode api --reload

```

### Run FastAPI with multiple workers (production)
```bash
poetry run python main.py --mode api --workers 4

```

### Run CLI (deprecated)
```bash
poetry run python main.py --mode cli interactive 

```
⚠️ CLI mode is deprecated. Prefer using the FastAPI API.

---

## 📡 Example API Usage

### Create Project
```Http
POST /projects
{
  "name": "My Project",
  "description": "First project"
}
``` 
### Patch Project
```Http
PATCH /projects/1
{
  "name": "Updated Project Name"
}

``` 

### Get Project by Name
```Http
GET /projects/by-name?name=My Project
``` 

### Create Task
```Http
POST /tasks
{
  "project_id": 1,
  "name": "Fix Bug",
  "description": "Resolve API issue",
  "status": "todo"
}
``` 

### Patch Task
```Http
PATCH /tasks/42
{
  "status": "done",
  "deadline": "2025-12-01T00:00:00"
}
``` 

### Get Task by Name
```Http
GET /tasks/by-name?name=Fix Bug
``` 
---

## 🛠️ Development Notes
- Use async def for controllers to support non‑blocking endpoints.

- Switch to AsyncSession in db/session.py if you want full async DB support.

- Background jobs run automatically on API startup via commands/scheduler.py.

---










