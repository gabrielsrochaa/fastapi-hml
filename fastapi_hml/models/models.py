from typing import Optional
from pydantic import BaseModel

class ModeloDoItem(BaseModel):
    titulo: str
    status: Optional[str]

