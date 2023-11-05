from pydantic import BaseModel, EmailStr, Field

class UserBaseSchema(BaseModel):
    name: str = Field(max_length=255)
    email: EmailStr = Field(max_length=255)
    address: str = Field(max_length=255)
    phone: str = Field(min_length=12, max_length=14)
    
    class Config:
        from_attributes = True


class CreateUserSchema(UserBaseSchema):
    password: str = Field(min_length=8, max_length=120)

class UserResponse(UserBaseSchema):
   id: int

class UpdateUserSchema(UserBaseSchema):
    pass
