from sqlalchemy import TIMESTAMP, Column, String, Boolean, text, Integer
from sqlalchemy.orm import relationship

from ..config.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(255),  nullable=False)
    password = Column(String(120),nullable=False)
    address = Column(String(255), nullable=False)
    phone = Column(String(14), unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=False), nullable=False, server_default=text("now()"))