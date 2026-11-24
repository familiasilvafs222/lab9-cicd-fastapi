
from fastapi import FastAPI

app = FastAPI(title="LAB9 - API DevOps")

@app.get("/")
def inicio():
    return {
        "mensagem": "API FastAPI funcionando!",
        "status": "OK"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}