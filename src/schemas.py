from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class TasksDTO(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime

class TasksPostDto(BaseModel):
    title: str
    description: Optional[str] = None