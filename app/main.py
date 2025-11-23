import argparse
import threading
import uvicorn
from fastapi import FastAPI
from api.routers import router
from cli.console import main as cli_main
from commands.scheduler import run_scheduler

# Create FastAPI app
app = FastAPI(
    title="Project & Task Manager",
    description="FastAPI backend for managing projects and tasks with periodic background jobs",
    version="1.0.0"
)

# Include all routers (projects, tasks, etc.)
app.include_router(router)

def start_scheduler():
    """Run periodic background tasks (e.g., autoclose overdue)."""
    run_scheduler()

def run_cli():
    print("⚠️ CLI mode is deprecated. Prefer using the FastAPI API instead.")
    cli_main()

def run_api(host: str = "127.0.0.1", port: int = 8000, reload: bool = False, workers: int = 1):
    # Start scheduler in background thread
    threading.Thread(target=start_scheduler, daemon=True).start()
    # Run FastAPI app via import string so reload/workers work
    uvicorn.run("main:app", host=host, port=port, reload=reload, workers=workers)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Unified entrypoint for CLI and FastAPI API")
    parser.add_argument("--mode", choices=["api", "cli"], default="api", help="Run mode: api or cli")
    parser.add_argument("--host", default="127.0.0.1", help="Host for API")
    parser.add_argument("--port", type=int, default=8000, help="Port for API")
    parser.add_argument("--reload", action="store_true", help="Enable auto-reload for API")
    parser.add_argument("--workers", type=int, default=1, help="Number of API workers")

    args, extra = parser.parse_known_args()

    if args.mode == "cli":
        run_cli()
    else:
        run_api(host=args.host, port=args.port, reload=args.reload, workers=args.workers)


