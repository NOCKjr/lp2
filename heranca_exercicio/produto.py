class Produto:
    _historico = []
    def __init__(self, nome, preco_compra = 0, quantidade_estoque = 0):
        self._nome = nome
        self._preco_compra = preco_compra
        self._quantidade_estoque = quantidade_estoque
        self._preco_venda = 0
    def definir_preco_venda(self, lucro = 0.4):
        self._preco_venda = self._preco_compra + (lucro * self._preco_compra)

    def vender_produto(self, qtde = 1):
        try:
            if self._quantidade_estoque < qtde:
                raise ValueError
            self._quantidade_estoque -= qtde
            Produto._historico.append(f'{qtde} unidade(s) vendida(s) de {self._nome}.')
            print("Produto vendido!")
        except ValueError:
            print("Quantidade indisponivel no estoque!")
    def comprar_produto(self, preco, qtde=1):
        try:
            if type(qtde) != int:
                raise ValueError
            Produto._historico.append(f'{qtde} unidade(s) comprada(s) de {self._nome}.')
            self._quantidade_estoque += qtde
            self._preco_compra = preco
            self.definir_preco_venda()
            print(f"{qtde} unidade(s) do produto: {self._nome}, foram adicionados ao estoque!")
        except ValueError:
            print('Valor invalido!')

    def mostrar_registro(self):
        for i in self._historico:
            print(i)

    def get_preco_venda(self):
        return self._preco_venda

    @property
    def preco_compra(self):
        return self._preco_compra

    @preco_compra.setter
    def preco_compra(self, valor):
        self._preco_compra = valor

    @property
    def quantidade_estoque(self):
        return self._quantidade_estoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, valor):
        self._quantidade_estoque = valor