import enum
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, UniqueConstraint
from sqlalchemy.orm import relationship
from db.base import Base

class TaskStatus(enum.Enum):
    todo = "todo"
    doing = "doing"
    done = "done"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    status = Column(Enum(TaskStatus), default=TaskStatus.todo, nullable=False)
    deadline = Column(DateTime)
    closed_at = Column(DateTime, nullable=True)

    project_id = Column(Integer, ForeignKey("projects.id"))
    project = relationship("Project", back_populates="tasks")

    __table_args__ = (
        UniqueConstraint("project_id", "name", name="uq_task_project_name"),
    )

