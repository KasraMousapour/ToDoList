from sqlalchemy.orm import Session
from repositories.task_repository import TaskRepository
from models.task import TaskStatus
from datetime import datetime
from exceptions.service_exceptions import ValidationError, LimitExceededError, DeadlineError
import os

MAX_TASKS_PER_PROJECT = int(os.getenv("MAX_TASKS_PER_PROJECT", 100))

class TaskService:
    def __init__(self, db: Session):
        self.task_repo = TaskRepository(db)

    def create_task(self, project_id: int, name: str, description: str = None,
                    status: TaskStatus = TaskStatus.todo, deadline=None):
        if len(name) < 30:
            raise ValidationError("Task name must be at least 30 characters long")
        if description and len(description) < 150:
            raise ValidationError("Task description must be at least 150 characters long")

        if deadline:
            if not isinstance(deadline, datetime):
                raise DeadlineError("The deadline format must be YYYY-MM-DD")
            if deadline <= datetime.now():
                raise DeadlineError("Deadline must be in the future")
            
        tasks = self.task_repo.list_by_project(project_id)
        if len(tasks) >= MAX_TASKS_PER_PROJECT:
            raise LimitExceededError(f"Cannot create more than {MAX_TASKS_PER_PROJECT} tasks in a project")    

        return self.task_repo.create(project_id, name, description, status, deadline)

    def update_task(self, task_id: int, **kwargs):
        task = self.task_repo.get(task_id)
        if not task:
            return None

        if "name" in kwargs:
            if len(kwargs["name"]) < 30:
                raise ValidationError("Task name must be at least 30 characters long")

        if "description" in kwargs and len(kwargs["description"]) < 150:
            raise ValidationError("Task description must be at least 150 characters long")

        if "deadline" in kwargs:
            deadline = kwargs["deadline"]
            if not isinstance(deadline, datetime):
                raise DeadlineError("The deadline format must be YYYY-MM-DD")
            if deadline <= datetime.now():
                raise DeadlineError("Deadline must be in the future")

        return self.task_repo.update(task_id, **kwargs)

    def change_status(self, task_id: int, new_status: TaskStatus):
        if new_status not in TaskStatus:
            raise ValidationError("Invalid status")
        return self.task_repo.update(task_id, status=new_status)

    def list_tasks_for_project(self, project_id: int):
        return self.task_repo.list_by_project(project_id)

    def delete_task(self, task_id: int):
        return self.task_repo.delete(task_id)
