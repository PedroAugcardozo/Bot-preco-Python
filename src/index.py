from Bots.amazon import pegarPreco as amazon
from Bots.mercadoLivre import pegarPreco as mercadoLivre
from Bots.kabum import pegarPreco as kabum
from database import criar_tabela, buscar_por_email, salvar_execucao
import smtplib
import email.message
import os
from dotenv import load_dotenv

load_dotenv()

def enviar_email(destinatario, nome, link):
    remetente = os.getenv('REMETENTE')
    senha = os.getenv('SENHA')

    corpo_email = f"""
    Olá com prazer viemos te informar que o preço do produto que você estava monitorando caiu!!
    O produto é: {nome}
    o link do produto é: {link}
    """
    msg = email.message.EmailMessage()
    msg['Subject'] = 'Notificação de redução de preço'
    msg['From'] = 'botparatext@gmail.com'
    msg['To'] = destinatario
    password = senha
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(remetente, password)
    s.sendmail(msg['From'],[msg['To']], msg.as_string().encode('utf-8'))
    print("Email enviado com sucesso!")


def controlar_bots(link: str, nome: str, email: str):
    if(nome == "amazon"):
        preco = amazon.pegarPreco(link)
    elif(nome == "mercadoLivre"):
        preco = mercadoLivre.pegarPreco(link)
    elif(nome == "kabum"):
        preco = kabum.pegarPreco(link)
    
    criar_tabela()
    dados = buscar_por_email(email)
    if dados == []:
        salvar_execucao(link, email, nome, preco)
    else:
        if dados.preco > preco:
            #aqui eu notifico o usuario da redução de preço
            enviar_email(email, nome, link)

    return "Bot executado com sucesso!"

    
