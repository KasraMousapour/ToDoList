import schedule
import time
from commands.autoclose_overdue import autoclose_overdue_tasks

def run_scheduler():
    # Run every 20 minutes
    schedule.every(20).minutes.do(autoclose_overdue_tasks)

    print("[SCHEDULER] Started. Running periodic jobs...")
    while True:
        schedule.run_pending()
        time.sleep(1)  # sleep to avoid busy loop