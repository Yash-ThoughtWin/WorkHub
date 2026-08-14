from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

from app.core.security import JWT_SECRET_KEY, JWT_ALGORITHM

from app.models.role import Role
from app.models.user import User
from app.database.session import get_db

from sqlalchemy.orm import Session


security = HTTPBearer()


def get_current_user_id(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )

        user_id = payload.get("sub")

        if not user_id:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return int(user_id)

    except (jwt.InvalidTokenError, ValueError):
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )


def require_role(required_role: str):

    def role_checker(
        user_id: int = Depends(get_current_user_id),
        db: Session = Depends(get_db)
    ):
        user = db.get(User, user_id)

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        role = db.get(Role, user.role_id)

        if not role or role.name != required_role:
            raise HTTPException(
                status_code=403,
                detail="Access forbidden"
            )

        return user

    return role_checker