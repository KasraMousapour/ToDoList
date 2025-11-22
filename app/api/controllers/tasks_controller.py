from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from services.task_services import TaskService
from models.task import TaskStatus
from api.controllers_schema import TaskCreateRequest, TaskUpdateRequest
from api.controllers_schema import TaskResponse
from exceptions.repository_exceptions import DuplicateNameError
from exceptions.service_exceptions import ValidationError, LimitExceededError, DeadlineError

router = APIRouter()

@router.post("/", response_model=TaskResponse)
def create_task(data: TaskCreateRequest, db: Session = Depends(get_db)):
    service = TaskService(db)
    try:
        task = service.create_task(
            project_id=data.project_id,
            name=data.name,
            description=data.description,
            status=data.status,
            deadline=data.deadline
        )
        return task
    except (ValidationError, DuplicateNameError, LimitExceededError, DeadlineError) as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/project/{project_id}", response_model=list[TaskResponse])
def list_tasks(project_id: int, db: Session = Depends(get_db)):
    service = TaskService(db)
    return service.list_tasks_for_project(project_id)

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, data: TaskUpdateRequest, db: Session = Depends(get_db)):
    service = TaskService(db)
    task = service.update_task(task_id, **data.dict(exclude_unset=True))
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    service = TaskService(db)
    success = service.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted"}
