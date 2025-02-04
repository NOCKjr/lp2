from conta import Conta
class Agencia:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []
        self.status = True

    def adicionarConta(self, numero, saldo, limite):
        if self.status:
            c1 = Conta(numero, saldo, limite)
            self.contas.append(c1)
            return True
        else:
            print(f"Agencia {self} foi encerrada!")
            return False

    def listarContas(self):
        print(f"contas da agencia: {self}")
        for c in self.contas:
            print(f"{c}")

    def fecharAgencia(self):
        while len(self.contas) > 0:
            self.contas.pop()
        self.status = False
        print(f'Agencia {self} encerrada!')

    def __str__(self):
        return f'{self.nome}'