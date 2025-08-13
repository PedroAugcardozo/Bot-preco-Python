import schedule
from src.index import bot_controlador
import time
from core.email import enviar_email

def controlar_tempo(link: str, nome: str, email: str):
    try:
        bot = bot_controlador(link, nome, email)
        schedule.every(5).hours.do(bot.controlar_bots, link=link, nome=nome, email=email)
        while bot.preco_atual >= bot.preco_original: 
            schedule.run_pending()
            time.sleep(1)
        if bot.preco_atual < bot.preco_original:
            enviar_email(email, nome, link)
            print(f"Preço do produto {nome} caiu para {bot.preco_atual}. Email enviado para {email}.")
            return f"Status 200: Preço do produto {nome} caiu para {bot.preco_atual}. Email enviado para {email}."
    except Exception as e:
        print(f"Erro ao agendar a tarefa: {e}")
        return "erro ao agendar tarefa"