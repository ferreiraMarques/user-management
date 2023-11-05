from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from sqlalchemy.orm import Session

from ..config.utils import hash_password, verify_phone
from ..schemas import user as userSchema
from ..models.user import User
from ..config.database import engine


def get_users(limit: int = 10, page: int = 1, search: str = ""):
    try:
        skip = (page - 1) * limit
        db = Session(engine)

        users = db.query(User).group_by(User.id).filter(
        User.email.contains(search)).limit(limit).offset(skip).all()
    
        return users
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                detail=str(ex))
    finally:
        db.close()
    

def get_user(id: int):
    try:    
        db = Session(engine)
        user = db.query(User).where(User.id == id).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found user with id: {id} found")
    
        return user
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                detail=str(ex))
    finally:
        db.close()


def create_user(data: userSchema.CreateUserSchema):
        db = Session(engine)
     
        verify_phone(data.phone)
  
        userPhone = db.query(User).where(User.phone == data.phone).first()
     
        if userPhone is not None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"phone is already in used")
             
        userEmail = db.query(User).where(User.email == data.email).first()

        if userEmail is not None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"email is already in used")

        new_user = User(**data.dict())
        new_user.password = hash_password(new_user.password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        db.close()

        return new_user

def update_user(id: int, data: userSchema.UpdateUserSchema, current_user: User):
        db = Session(engine)
        verify_phone(data.phone)

        user_query = db.query(User).filter(User.id == id)
        
        if not user_query:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found user with id: {id} found")

        if current_user.id != id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"unAuthorized")
        
        userPhone: User = db.query(User).where(User.phone == data.phone).first()
     
        if userPhone is not None and userPhone.id != id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"phone is already in used")
             
        userEmail:User = db.query(User).where(User.email == data.email).first()

        if userEmail is not None and userEmail.id != id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"email is already in used")

        user: User = user_query.first()
        user.address = data.address
        user.phone = data.phone
        user.email = data.email
        user.name = data.name

        db.add(user)
        db.commit()

        db.close()        
        return db.query(User).where(User.id == id).first()


def delete_user(id: int):
    try:
        db = Session(engine)
        user_query = db.query(User).filter(User.id == id)
        user = user_query.first()

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found user with id: {id} found")

        user_query.delete(synchronize_session=False)
    
        db.commit()

    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=str(ex))
    finally:
        db.close()