from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    """
    Root view, retorna {"hello": "world"}
    """
    return {"hello":"world"}
