from pydantic import BaseModel
from datetime import datetime
from models.task import TaskStatus

class TaskCreateRequest(BaseModel):
    project_id: int
    name: str
    description: str
    status: TaskStatus = TaskStatus.todo
    deadline: datetime | None = None

class TaskUpdateRequest(BaseModel):
    name: str | None = None
    description: str | None = None
    status: TaskStatus | None = None
    deadline: datetime | None = None
