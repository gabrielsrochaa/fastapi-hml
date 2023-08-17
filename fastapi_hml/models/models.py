from typing import Optional
from pydantic import BaseModel

class ModeloDoItem(BaseModel):
    id: int
    titulo: str
    status: Optional[str]

