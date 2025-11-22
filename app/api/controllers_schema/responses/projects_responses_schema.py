from pydantic import BaseModel

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True
