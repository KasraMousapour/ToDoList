from pydantic import BaseModel
from datetime import datetime
from models.task import TaskStatus

class TaskResponse(BaseModel):
    id: int
    project_id: int
    name: str
    description: str
    status: TaskStatus
    deadline: datetime | None
    closed_at: datetime | None

    class Config:
        orm_mode = True
