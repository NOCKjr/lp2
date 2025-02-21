from produto import Produto
class ProdutoParcelado(Produto):
    def __init__(self, nome, preco_compra = 0, quantidade_estoque = 0):
        super().__init__(nome, preco_compra, quantidade_estoque)
        self._preco_venda += self.definir_preco_venda()
    def definir_preco_venda(self):
        return (0.05 * self._preco_compra)
