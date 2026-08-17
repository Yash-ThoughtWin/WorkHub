from pydantic import BaseModel


class ProjectCreate(BaseModel):
    name: str
    description: str | None = None

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str | None
    status: str
    owner_id: int

    model_config = {
        "from_attributes": True
    }

class ProjectUpdate(BaseModel):
    name: str
    description: str | None = None
    status: str