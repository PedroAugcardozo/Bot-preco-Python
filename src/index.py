from Bots.amazon import robo as amazon
from Bots.mercadoLivre import robo as mercadoLivre
from Bots.kabum import robo as kabum
from database import criar_tabela, atualizar_preco, buscar_por_telefone, salvar_execucao

def controlar_bots(link: str, nome: str, telefone: str):
    if(nome == "amazon"):
        preco = amazon.pegarPreco(link)
    elif(nome == "mercadoLivre"):
        preco = mercadoLivre.pegarPreco(link)
    elif(nome == "kabum"):
        preco = kabum.pegarPreco(link)
    
    criar_tabela()
    dados = buscar_por_telefone(telefone)
    if dados == []:
        salvar_execucao(link, telefone, nome, preco)
    else:
        if dados.preco > preco:
            #aqui eu notifico o usuario da redução de preço
            atualizar_preco(telefone, preco)

    return "Bot executado com sucesso!"

    
