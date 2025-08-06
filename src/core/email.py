import email.message
import os
from dotenv import load_dotenv
import smtplib

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