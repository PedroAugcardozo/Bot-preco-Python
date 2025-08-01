from fastapi import FastAPI
from pydantic import BaseModel
from src.index import controlar_bots

app = FastAPI()

#rota get
@app.get("/")
def home():
    return {"message": "Bem-vindo ao bot de comparação de preços!"}

class dadosRequest(BaseModel):
    link: str
    nome: str
    email: str

# cria os bots
@app.post("/bots")
async def criar_bots(dados: dadosRequest):
    resultado = await controlar_bots(
        dados.link,
        dados.nome,
        dados.email
    )
    return {"resultado": resultado}

