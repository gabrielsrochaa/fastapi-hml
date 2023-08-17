from typing import List, Dict, Any

class AFazer:
    todo: List[Dict[str, Any]] = [
        {"id":1, "titulo":"Fazer live", "status": "A Fazer"},
        {"id":2, "titulo":"Ligar Streaming", "status":"A Fazer"},
        {"id":3, "titulo":"Pentear o cabelo", "status":"A Fazer"}
    ]
    id_atual = 3

    def listar(self):
        return self.todo

    def inserir(self, item: Dict[str, Any]) -> Dict[str, Any] :
        self.id_atual += 1
        item["id"] = self.id_atual
        self.todo.append(item)
        return item
