import schedule
from src.index import bot_controlador
import time

def controlar_tempo(link: str, nome: str, email: str):
    try:
        bot = bot_controlador(link, nome, email)
        schedule.every(5).hours.do(bot.controlar_bots, link=link, nome=nome, email=email)
        while bot.preco : 
            schedule.run_pending()
            time.sleep(1)
    except Exception as e:
        print(f"Erro ao agendar a tarefa: {e}")
        return "erro ao agendar tarefa"