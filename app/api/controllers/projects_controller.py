from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from services.project_services import ProjectService
from api.controllers_schema import ProjectCreateRequest, ProjectUpdateRequest
from api.controllers_schema import ProjectResponse
from exceptions.repository_exceptions import DuplicateNameError
from exceptions.service_exceptions import ValidationError, LimitExceededError

router = APIRouter()

@router.post("/", response_model=ProjectResponse)
def create_project(data: ProjectCreateRequest, db: Session = Depends(get_db)):
    service = ProjectService(db)
    try:
        project = service.create_project(name=data.name, description=data.description)
        return project
    except (ValidationError, DuplicateNameError, LimitExceededError) as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[ProjectResponse])
def list_projects(db: Session = Depends(get_db)):
    service = ProjectService(db)
    return service.project_repo.list()

@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(project_id: int, data: ProjectUpdateRequest, db: Session = Depends(get_db)):
    service = ProjectService(db)
    project = service.update_project(project_id, **data.dict(exclude_unset=True))
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.patch("/{project_id}", response_model=ProjectResponse)
def patch_project(project_id: int, data: ProjectUpdateRequest, db: Session = Depends(get_db)):
    """
    Partially update a project. Only provided fields will be updated.
    """
    service = ProjectService(db)
    update_data = data.dict(exclude_unset=True)  # only fields sent by client
    project = service.update_project(project_id, **update_data)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    service = ProjectService(db)
    success = service.delete_project(project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"detail": "Project deleted"}
