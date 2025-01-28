class Funcionario:
    def __init__(self, id, nome, cargo):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.projetos = []

    def __str__(self):
        return f'Nome: {self.nome} {self.id}'

    def listar_projetos(self):
        for p in self.projetos:
            print(f'{p.projeto.nome} | {p.papel} | {p.data_inicio}')
        print(f"Total de participações de projetos: {len(self.projetos)}")