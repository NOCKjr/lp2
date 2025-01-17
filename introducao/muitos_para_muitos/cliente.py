from cliente_conta import ClienteConta
class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")

    def adicionar_conta(self, conta, tipo):
        #objeto que interliga conta e cliente
        obj_intermediario = ClienteConta(self, conta, tipo)
        #adiciona nas listas de cada
        self.contas.append(obj_intermediario)
        conta.clientes.append(obj_intermediario)

    def listar_contas(self):
        print(f'Contas do cliente {self.nome}:')
        for cc in self.contas:
            print(f"{cc.conta}")

    def __str__(self):
        return f'{self.nome}'
