from typing import Optional
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    __tablename__ = 'users'

    id: Optional[int] = Field(default=None, nullable=True, primary_key=True)
    email: str = Field(unique=True, index=True)
    name: str 
    password: str