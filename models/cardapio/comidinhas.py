from models.cardapio import Cardapio

class Comidinhas(Cardapio):
    def __init__(self, nome, preco, tipo, ingredientes):
        super().__init__(nome, preco, tipo, ingredientes)
    
    def __str__(self):
        return self.nome