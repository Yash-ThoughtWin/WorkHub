from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role_id: int

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role_id: int
    is_active: bool

    model_config = {
        "from_attributes": True
    }

class UserUpdate(BaseModel):
    name: str
    email: EmailStr
    role_id: int