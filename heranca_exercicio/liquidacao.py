from produto import Produto
class Liquidacao:
    def __init__(self):
        pass

    def adicionar_liquidacao(self, produto):
        produto._preco_venda -= produto._preco_venda/2
        print(f'Preço do produto {produto.get_nome()} ta liquidado!')