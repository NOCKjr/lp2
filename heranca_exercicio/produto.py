class Produto:
    def __init__(self, nome, preco_compra = 0, quantidade_estoque = 0):
        self._nome = nome
        self._preco_compra = preco_compra
        self._quantidade_estoque = quantidade_estoque
        self._preco_venda = self.preco_venda()
        self._historico = []
    def preco_venda(self):
        return (self._preco_compra + (0.10 * self._preco_compra))

    def vender_produto(self, qtde = 1):
        try:
            if self._quantidade_estoque == 0:
                raise ValueError('Fora de estoque!')
            if qtde > self._quantidade_estoque:
                raise ValueError('Quantidade ultrapassa do estoque.')
            self._quantidade_estoque -= qtde
            self._historico.append(f'Venda de {qtde} unidade(s).')
            print("Produto vendido!")
        except ValueError:
            pass

    def comprar_produto(self, qtde:int):
        try:
            if type(qtde) == int:
                raise ValueError
            self._historico.append(f'compra de {qtde} unidade(s).')
            self._quantidade_estoque += qtde
            print(f"{qtde} unidade(s) do produto: {self._nome}, foram adicionados ao estoque!")
        except ValueError:
            print('Valor invalido!')

    def get_preco_venda(self):
        return self._preco_venda

    def get_nome(self):
        return self._nome