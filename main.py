from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import BackgroundTasks

app = FastAPI()

#rota get
@app.get("/")
def home():
    return {"message": "Bem-vindo ao bot de comparação de preços!"}

class dadosRequest(BaseModel):
    link: str
    nome: str
    email: str

#manter o agendamento ativo
bot_schedule = {}

# cria os bots
@app.post("/bots")
async def criar_bots(dados: dadosRequest, background_tasks: BackgroundTasks):
    return("mensagem: Bot criado com sucesso!")

