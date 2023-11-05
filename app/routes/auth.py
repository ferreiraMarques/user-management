from fastapi import APIRouter, Request, Response, status, Depends, HTTPException

from ..services import auth_service
from ..schemas.auth import LoginUserSchema
from ..models.user import User

router = APIRouter()

@router.post('/login')
def login(payload: LoginUserSchema, response: Response):

    user: User = auth_service.authenticate_user(payload.phone, payload.password)
    access_token: str = auth_service.generate_token(user)

    return {
        "user": 
        {
            "id": user.id,
            "name": user.name,
            "session_active": True,
            "email": user.email,
            "phone":  user.phone,
            "address": user.address
        },
        "access_token": access_token, 
        "token_type": "bearer"
    }

