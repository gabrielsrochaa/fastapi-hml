from typing import Optional
from pydantic import BaseModel
from database.data import OpcoesDeStatus

class ModeloDoItem(BaseModel):
    titulo: str
    status: Optional[OpcoesDeStatus]

class ModeloDoItemResposta(ModeloDoItem):
    id: int