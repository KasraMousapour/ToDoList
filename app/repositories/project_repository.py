from sqlalchemy.orm import Session
from models.project import Project

class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str, description: str = None) -> Project:
        project = Project(name=name, description=description)
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def get(self, project_id: int) -> Project | None:
        return self.db.query(Project).filter(Project.id == project_id).first()

    def list(self) -> list[Project]:
        return self.db.query(Project).all()

    def update(self, project_id: int, **kwargs) -> Project | None:
        project = self.get(project_id)
        if not project:
            return None
        for key, value in kwargs.items():
            setattr(project, key, value)
        self.db.commit()
        self.db.refresh(project)
        return project

    def delete(self, project_id: int) -> bool:
        project = self.get(project_id)
        if not project:
            return False
        self.db.delete(project)
        self.db.commit()
        return True
