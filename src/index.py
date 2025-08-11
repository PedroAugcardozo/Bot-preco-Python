from Bots.amazon import pegarPreco as amazon
from Bots.mercadoLivre import pegarPreco as mercadoLivre
from Bots.kabum import pegarPreco as kabum
from core.email import enviarEmail

class bot_controlador:
    __preco_original = None;
    __Preco_atual = None
    __Primeiro_Preco = True;

    def __init__(self, link: str, nome: str, email: str):
        self.link = link
        self.nome = nome
        self.email = email

    def controlar_bots(self):
        if(self.nome == "amazon"):
            self.preco_atual = amazon.pegarPreco(self.link)
        elif(self.nome == "mercadoLivre"):
            self.preco_atual = mercadoLivre.pegarPreco(self.link)
        elif(self.nome == "kabum"):
            self.preco_atual = kabum.pegarPreco(self.link)

        if(self.Primeiro_preco):
            self.Primeiro_preco = False
            self.preco_original = self.precoAtual
        
        if(self.preco_atual < self.preco_original):
            enviarEmail(self.Destinatario, self.nome, self.link)
            print(f"Preço do produto {self.nome} caiu para {self.preco_atual}. Email enviado para {self.email}.")
            return f"Status 200: Preço do produto {self.nome} caiu para {self.preco_atual}. Email enviado para {self.email}."

    
    @property
    def precoAtual(self):
        return self.__Preco_atual
    
    @property
    def precoOriginal(self):
        return self.__preco_original
    
    @property
    def Primeiro_preco(self):
        return self.__Primeiro_Preco