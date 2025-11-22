from datetime import datetime
from db.session import SessionLocal
from models.task import Task, TaskStatus

def autoclose_overdue_tasks():
    """Find tasks past their deadline and mark them as done with closed_at timestamp."""
    db = SessionLocal()
    try:
        now = datetime.now()
        overdue_tasks = (
            db.query(Task)
            .filter(Task.deadline < now, Task.status != TaskStatus.done)
            .all()
        )

        for task in overdue_tasks:
            task.status = TaskStatus.done
            task.closed_at = now
            print(f"[AUTO-CLOSE] Task {task.id} ({task.name}) closed at {now}")

        db.commit()
    finally:
        db.close()