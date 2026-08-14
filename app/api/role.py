from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.role import Role
from app.schemas.role import RoleCreate


router = APIRouter()


@router.post("/roles")
def create_role(role: RoleCreate, db: Session = Depends(get_db)):

    new_role = Role(name=role.name)

    db.add(new_role)
    db.commit()
    db.refresh(new_role)

    return new_role