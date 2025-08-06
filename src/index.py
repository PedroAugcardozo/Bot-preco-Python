from Bots.amazon import pegarPreco as amazon
from Bots.mercadoLivre import pegarPreco as mercadoLivre
from Bots.kabum import pegarPreco as kabum


def controlar_bots(link: str, nome: str, email: str):
    if(nome == "amazon"):
        preco = amazon.pegarPreco(link)
    elif(nome == "mercadoLivre"):
        preco = mercadoLivre.pegarPreco(link)
    elif(nome == "kabum"):
        preco = kabum.pegarPreco(link)
    else:
        return "Bot não encontrado"
    return "Bot executado com sucesso!"