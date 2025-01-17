from historico import Historico
class Conta:
    def __init__(self, numero, saldo, limite):
        self.numero = numero
        self.clientes = []
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def sacar(self, valor):
        if valor<=self.saldo:
            self.saldo -= valor
            self.historico.transacoes.append(f"Saque de {valor}!")
            return True
        else:
            return False
    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f"Depósito de {valor}!")
        return True
    def ver_saldo(self):
        return self.saldo

    def transferir(self, destino, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"{self.titulo} transferiu {valor:.2f} R$ para {destino.titulo}.")
            self.historico.transacoes.append(f"Transferencia de {valor} para {destino}")
            destino.historico.transacoes.append(f'')
        else:
            return False

    def listar_clientes(self):
        print(f"clientes da conta {self.numero}:")
        for cl in self.clientes:
            print(f"{cl.cliente}")

    def __str__(self):
        return (f'numero: {self.numero}')