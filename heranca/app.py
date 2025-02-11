from gerente import Gerente
from funcionario import Funcionario
from controle_de_bonificacoes import ControleDeBonificacoes
f1 = Funcionario('Fulano', 5000, '094343957253')
g1 = Gerente("elias", 9000, '06064218231', 12345, 5)
print(f1.get_bonificacao())
print(g1.get_bonificacao())
controle = ControleDeBonificacoes()
controle.registra(f1)
controle.registra(g1)
print(controle.get_total())