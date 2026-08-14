from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.database.session import get_db
from app.models.role import Role
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin, UserResponse, UserUpdate

from app.core.security import create_access_token, verify_password
from app.schemas.user import UserCreate, UserLogin

from app.core.dependencies import get_current_user_id, require_role

router = APIRouter()

@router.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    role = db.get(Role, user.role_id)

    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=hash_password(user.password),
        role_id=user.role_id
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email,
        "role_id": new_user.role_id
    }

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(db_user.id)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/me")
def get_me(
    user_id: int = Depends(get_current_user_id),
    db: Session = Depends(get_db)
):
    user = db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role_id": user.role_id
    }

@router.get("/admin-test")
def admin_test(
    user: User = Depends(require_role("ADMIN"))
):
    return {
        "message": "Welcome Admin"
    }

@router.get("/users", response_model=List[UserResponse])
def get_users(
    db: Session = Depends(get_db)
):
    return db.query(User).all()


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):
    user = db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    role = db.get(Role, user_data.role_id)

    if not role:
        raise HTTPException(
            status_code=404,
            detail="Role not found"
        )

    user.name = user_data.name
    user.email = user_data.email
    user.role_id = user_data.role_id

    db.commit()
    db.refresh(user)

    return user

@router.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }

@router.patch("/users/{user_id}/deactivate")
def deactivate_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.is_active = False

    db.commit()

    return {
        "message": "User deactivated successfully"
    }

@router.patch("/users/{user_id}/activate")
def activate_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.is_active = True

    db.commit()

    return {
        "message": "User activated successfully"
    }