from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.project import Project
from exceptions.repository_exceptions import DuplicateNameError

class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str, description: str = None) -> Project:
        project = Project(name=name, description=description)
        self.db.add(project)
        try:
            self.db.commit()
            self.db.refresh(project)
            return project
        except IntegrityError as e:
            self.db.rollback()
            # Translate DB-level error into custom exception
            raise DuplicateNameError("Project name must be unique") from e

    def get_by_id(self, project_id: int) -> Project | None:
        return self.db.query(Project).filter(Project.id == project_id).first()

    def list(self) -> list[Project]:
        return self.db.query(Project).all()

    def update(self, project_id: int, **kwargs) -> Project | None:
        project = self.get_by_id(project_id)
        if not project:
            return None
        for key, value in kwargs.items():
            setattr(project, key, value)
        try:
            self.db.commit()
            self.db.refresh(project)
            return project
        except IntegrityError as e:
            self.db.rollback()
            raise DuplicateNameError("Project name must be unique") from e

    def delete(self, project_id: int) -> bool:
        project = self.get_by_id(project_id)
        if not project:
            return False
        self.db.delete(project)
        self.db.commit()
        return True
