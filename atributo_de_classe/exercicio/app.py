from produto import Produto
p1 = Produto('banana', 100)
p2 = Produto('feijao', 500)

print(p1.preco)
Produto.atualizar_desconto(34)
print(p1.preco)

p3 = Produto('sla', -1123)
print(p3.preco)