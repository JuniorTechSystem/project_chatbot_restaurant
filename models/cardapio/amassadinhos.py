from models.cardapio import Cardapio

class Amassadinhos(Cardapio):
    def __init__(self, nome, preco, ingredientes, tipo, ingrediente_especial):
        super().__init__(nome, preco, ingredientes, tipo)
        self.ingrediente_especial = ingrediente_especial
    
    def __str__(self):
        return self._nome
    