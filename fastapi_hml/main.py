from fastapi import FastAPI
from typing import List, Dict, Any
from models.models import ModeloDoItem

todo: List[Dict[str, Any]] = [
    {"id":1, "titulo":"Fazer live", "descricao":"Fazer live no canal do Edu"},
    {"id":2, "titulo":"Ligar Streaming", "status":"A Fazer"},
    {"id":3, "titulo":"Pentear o cabelo", "status":"A Fazer"}
]

app = FastAPI()

@app.get("/")
def hello_world():
    """
    Root view, retorna {"hello": "world"}
    """
    return {"hello":"world"}

@app.get("/a-fazer", response_model=List[ModeloDoItem])
def listar_a_fazer():
    """
    View que retorna lista de itens a fazer
    """
    return todo