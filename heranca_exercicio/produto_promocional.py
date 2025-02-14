from produto import Produto
class ProdutoPromocional(Produto):
    def __init__(self, nome, preco_compra = 0, quantidade_estoque = 0):
        super().__init__(nome, preco_compra, quantidade_estoque)
        self._preco_venda -= self.preco_venda()
    def preco_venda(self):
        return (0.20 * self._preco_compra)

