from pydantic import BaseModel, Field

class LoginUserSchema(BaseModel):
    phone: str = Field(min_length=12, max_length=14)
    password: str = Field(min_length=8, max_length=120)
    
    class Config:
        from_attributes = True
