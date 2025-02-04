from projeto import Projeto
from funcionario import Funcionario
p1 = Projeto(1, 'projeto 1', "teste")
p2 = Projeto(2, 'projeto 2', "teste")

f1 = Funcionario(1, 'Fulano', "gerente")
f2 = Funcionario(2, 'ciclano', 'Diretor')
f3 = Funcionario(3, 'beltrano', "estagiario")

p1.adicionar_funcionario(f1, 'Scrum master', '01/01/2025')
p1.adicionar_funcionario(f2, 'PO', '15/01/2025')
p2.adicionar_funcionario(f1, 'Scrum master', '01/01/2025')
p1.adicionar_funcionario(f3, 'Frontend', '01/01/2025')

p1.listar_funcionarios()
p1.remover_funcionario(f1)
p1.listar_funcionarios()
p2.listar_funcionarios()

f1.listar_projetos()
