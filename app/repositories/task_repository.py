from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.task import Task, TaskStatus
from exceptions.repository_exceptions import DuplicateNameError

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, project_id: int, name: str, description: str = None,
               status=None, deadline=None) -> Task:
        task = Task(
            project_id=project_id,
            name=name,
            description=description,
            status=status,
            deadline=deadline
        )
        self.db.add(task)
        try:
            self.db.commit()
            self.db.refresh(task)
            return task
        except IntegrityError as e:
            self.db.rollback()
            raise DuplicateNameError("Task name must be unique within the project") 

    def get_by_id(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.id == task_id).first()

    def list_by_project(self, project_id: int) -> list[Task]:
        return self.db.query(Task).filter(Task.project_id == project_id).all()

    def update(self, task_id: int, **kwargs) -> Task | None:
        task = self.get_by_id(task_id)
        if not task:
            return None
        for key, value in kwargs.items():
            setattr(task, key, value)
        try:
            self.db.commit()
            self.db.refresh(task)
            return task
        except IntegrityError as e:
            self.db.rollback()
            raise DuplicateNameError("Task name must be unique within the project")

    def delete(self, task_id: int) -> bool:
        task = self.get_by_id(task_id)
        if not task:
            return False
        self.db.delete(task)
        self.db.commit()
        return True
