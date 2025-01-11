from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class TaskBase(BaseModel):
    title: str
    description: str = None
    due_date: datetime = None

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    status: bool

    class Config:
        orm_mode = True
