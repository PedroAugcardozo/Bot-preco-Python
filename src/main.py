from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import BackgroundTasks
from core.schedule import controlar_tempo

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
async def criar_bots(dados: dadosRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(controlar_tempo, dados.link, dados.nome, dados.email)
    print(f"Bot criado para o produto {dados.nome} com link {dados.link}")
    return("mensagem: Bot criado com sucesso!")
