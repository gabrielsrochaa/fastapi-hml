from fastapi import FastAPI
from database.data import AFazer
from typing import List
from database.models import ModeloDoItem, ModeloDoItemResposta

a_fazer = AFazer()
app = FastAPI()

@app.get("/")
def hello_world():
    """
    Root view, retorna {"hello": "world"}
    """
    return {"hello":"world"}

@app.get("/a-fazer", response_model=List[ModeloDoItemResposta])
def listar_a_fazer():
    """
    View que retorna lista de itens a fazer
    """
    return a_fazer.listar()

@app.post("/a-fazer", response_model=ModeloDoItemResposta, status_code=201)
def inserir_a_fazer(item_a_inserir: ModeloDoItem):
    """
    View que insere item na lista a de intens a fazer
    """
    return a_fazer.inserir(item_a_inserir.dict())

@app.get("/a-fazer/{id_do_item}", response_model=ModeloDoItemResposta)
def pegar_item(id_do_item: int):
    """
    View que mostra o item pelo id
    """
    return a_fazer.pegar_item(id_do_item)
