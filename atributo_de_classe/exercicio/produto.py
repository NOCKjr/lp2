class Produto:
    _desconto = 0
    def __init__(self, nome, preco):
        if self.valida_preco(preco):
            self._nome = nome
            self._preco = preco

    @classmethod
    def atualizar_desconto(cls, novo_desconto):
        cls._desconto = novo_desconto
        print(f'Desconto atualizado para {novo_desconto}%')

    @staticmethod
    def valida_preco(preco):
        if(preco<0):
            raise ValueError("Não pode ser negativo")
        else:
            return True

    @property
    def preco(self):
        return self._preco - (Produto._desconto/100)*self._preco