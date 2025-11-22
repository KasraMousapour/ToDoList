import threading
from cli.console import main as cli_main
from commands.scheduler import run_scheduler

def start_scheduler():
    run_scheduler()

if __name__ == "__main__":
    # Run scheduler in background thread
    scheduler_thread = threading.Thread(target=start_scheduler, daemon=True)
    scheduler_thread.start()

    # Run CLI in foreground
    cli_main()
