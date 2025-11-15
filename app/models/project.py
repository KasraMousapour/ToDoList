from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship
from db.base import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String)

    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")

    __table_args__ = (
        UniqueConstraint("name", name="uq_project_name"),
    )
