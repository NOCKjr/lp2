from produto import Produto
from produto_parcelado import ProdutoParcelado
from produto_promocional import ProdutoPromocional
banana = Produto('banana', 2, 5)
banana.comprar_produto(5, 4)
banana.vender_produto(11)
banana.mostrar_registro()
banana.vender_produto(8)
banana.mostrar_registro()
print(banana.get_preco_venda())
print()
maca = ProdutoParcelado('maca', 5, 7)
maca.comprar_produto(3)
maca.vender_produto(5)
maca.mostrar_registro()
print(maca.get_preco_venda())

cachaca = ProdutoPromocional('cachaca', '7', '9')
cachaca.comprar_produto(3)
cachaca.vender_produto(5)
cachaca.mostrar_registro()
print(cachaca.get_preco_venda())