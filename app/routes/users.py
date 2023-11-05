from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from ..config.utils import hash_password, verify_phone
from ..schemas import user as userSchema
from ..models.user import User
from ..services import user_service
from ..services.auth_service import get_current_user 

router = APIRouter()

@router.get("/", response_model=List[userSchema.UserResponse])
def get_users(limit: int = 10, page: int = 1, search: str = "", current_user: User = Depends(get_current_user)):    
    return user_service.get_users(limit, page, search)

@router.get("/{id}", response_model=userSchema.UserResponse)
def get_user(id: int, current_user: User = Depends(get_current_user)):
    return user_service.get_user(id)

@router.post("/", response_model=userSchema.UserResponse)
def create_user(data: userSchema.CreateUserSchema, current_user: User = Depends(get_current_user)):
    return user_service.create_user(data)

@router.put("/{id}", response_model=userSchema.UserResponse)
def update_user(id: int, data: userSchema.UpdateUserSchema, current_user: User = Depends(get_current_user)):
    return user_service.update_user(id, data, current_user)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, current_user: User = Depends(get_current_user)):
    user_service.delete_user(id)