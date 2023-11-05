from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from ..models.user import User as UserModel
from ..schemas.auth import LoginUserSchema
from ..schemas.user import UserResponse
from ..config.config import Settings
from ..config.database import engine
from ..config.utils import verify_password

settings = Settings()

SECRET_KEY = settings.JWT_PRIVATE_KEY
ALGORITHM = settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRES_IN

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/users/login")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def generate_token(user: UserResponse):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect phone or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

def get_user(phone: str):
    try:
        db = Session(engine)
        return db.query(UserModel).where((UserModel.phone == phone) | (UserModel.phone == phone)).first()
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                detail=str(ex))
    finally:
        db.close()

def get_user_by_email(email: str):
    try:
        db = Session(engine)
        return db.query(UserModel).where((UserModel.email == email) | (UserModel.email == email)).first()
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                detail=str(ex))
    finally:
        db.close()

def authenticate_user(phone: str, password: str):
    user = get_user(phone)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")

        if email is None:
            raise credentials_exception
       
        token_data = email

    except JWTError:
        raise credentials_exception

    user = get_user_by_email(email=token_data)

    if user is None:
        raise credentials_exception
    return user
