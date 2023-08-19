from typing import List, Dict, Any, Union
from enum import Enum

class OpcoesDeStatus(str, Enum):
    a_fazer = "A Fazer"
    fazendo = "Fazendo"
    feito = "Feito"

Item = Dict[str, Union[int, str, OpcoesDeStatus]]

class AFazer:
    todo: List[Item] = [
        {"id":1, "titulo":"Fazer live", "status": OpcoesDeStatus.a_fazer},
        {"id":2, "titulo":"Ligar Streaming", "status":OpcoesDeStatus.a_fazer},
        {"id":3, "titulo":"Pentear o cabelo", "status":OpcoesDeStatus.a_fazer}
    ]
    id_atual = 3

    def listar(self):
        return self.todo

    def inserir(self, item: Item) -> Item :
        self.id_atual += 1
        item["id"] = self.id_atual
        self.todo.append(item)
        return item

    def pegar_item(self, id_do_item: int) -> Item:
        item = filter(lambda x: x["id"] == id_do_item, self.todo)
        return list(item)[0]
