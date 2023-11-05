import phonenumbers
from passlib.context import CryptContext
from fastapi import HTTPException, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)


def verify_phone(phone: str):
    phone_number = phonenumbers.parse(phone)

    if(phonenumbers.is_possible_number(phone_number) is False):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid phone number")