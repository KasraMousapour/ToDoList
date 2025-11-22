from fastapi import APIRouter
from api.controllers import projects_controller, tasks_controller

router = APIRouter()

router.include_router(projects_controller.router, prefix="/projects", tags=["Projects"])
router.include_router(tasks_controller.router, prefix="/tasks", tags=["Tasks"])
