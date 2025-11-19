from sqlalchemy.orm import Session
from repositories.project_repository import ProjectRepository
from repositories.task_repository import TaskRepository
from exceptions.service_exceptions import ValidationError, LimitExceededError
import os

MAX_PROJECTS = int(os.getenv("MAX_PROJECTS", 100))

class ProjectService:
    def __init__(self, db: Session):
        self.project_repo = ProjectRepository(db)
        self.task_repo = TaskRepository(db)

    def create_project(self, name: str, description: str = None):
        if len(name) > 50:
            raise ValidationError("Project name must be at the most 50 characters long")
        if description and len(description) > 150:
            raise ValidationError("Project description must be at the most 150 characters long")

        existing = self.project_repo.list()        
        if len(existing) >= MAX_PROJECTS:
            raise LimitExceededError(f"Cannot create more than {MAX_PROJECTS} projects")

        return self.project_repo.create(name=name, description=description)

    def update_project(self, project_id: int, **kwargs):
        if "name" in kwargs and len(kwargs["name"]) > 50:
            raise ValidationError("Project name must be at the most 50 characters long")
        if "description" in kwargs and len(kwargs["description"]) > 150:
            raise ValidationError("Project description must be at the most 150 characters long")

        return self.project_repo.update(project_id, **kwargs)

    def get_project_with_tasks(self, project_id: int):
        project = self.project_repo.get_by_id(project_id)
        if not project:
            return None
        tasks = self.task_repo.list_by_project(project_id)
        return {"project": project, "tasks": tasks}

    def delete_project(self, project_id: int):
        return self.project_repo.delete(project_id)

