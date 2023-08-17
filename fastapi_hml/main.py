from fastapi import FastAPI
from data import AFazer
from typing import List
from models.models import ModeloDoItem

a_fazer = AFazer()
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
    return a_fazer.listar()

@app.post("/a-fazer", response_model=ModeloDoItem, status_code=201)
def inserir_a_fazer(item_a_inserir: ModeloDoItem):
    """
    View que insere item na lista a de intens a fazer
    """
    return a_fazer.inserir(item_a_inserir.dict())