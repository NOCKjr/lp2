from projetoFuncionario import ProjetoFuncionario
class Projeto:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.funcionarios = []

    def listar_funcionarios(self):
        print(f"Funcionarios do projeto {self}")
        for f in self.funcionarios:
            print(f.funcionario)
        print(f"Total de funcionarios: {len(self.funcionarios)}")

    def adicionar_funcionario(self, funcionario, papel, data):
        assoc = ProjetoFuncionario(self, funcionario, papel, data)
        self.funcionarios.append(assoc)
        funcionario.projetos.append(assoc)

    def remover_funcionario(self, funcionario):
        func_remover = None
        for item in self.funcionarios:
            if item.funcionario.id == funcionario.id:
                func_remover = item
                break
        if func_remover:
            self.funcionarios.remove(func_remover)
            funcionario.projetos.remove(func_remover)
            print("funcionario removido!")

    def __str__(self):
        return f'projeto : {self.id}, nome {self.nome}'