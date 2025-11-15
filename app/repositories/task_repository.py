from sqlalchemy.orm import Session
from models.task import Task, TaskStatus

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, project_id: int, name: str, description: str = None,
               status: TaskStatus = TaskStatus.todo, deadline=None) -> Task:
        task = Task(
            project_id=project_id,
            name=name,
            description=description,
            status=status,
            deadline=deadline
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.id == task_id).first()

    def list_by_project(self, project_id: int) -> list[Task]:
        return self.db.query(Task).filter(Task.project_id == project_id).all()

    def update(self, task_id: int, **kwargs) -> Task | None:
        task = self.get(task_id)
        if not task:
            return None
        for key, value in kwargs.items():
            setattr(task, key, value)
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete(self, task_id: int) -> bool:
        task = self.get(task_id)
        if not task:
            return False
        self.db.delete(task)
        self.db.commit()
        return True
