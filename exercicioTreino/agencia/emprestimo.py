class Emprestimo:
    def __init__(self,conta, valor, parcelas):
        self.valor = valor
        self.parcelas = parcelas
        self.valor_parcela = valor/parcelas
        self.parcelas_restantes = parcelas
        self.conta = conta
        self.conta.depositar(valor)

    def pagarParcela(self):
        if self.parcelas_restantes>0:
            if self.conta.saldo >= self.valor_parcela:
                self.conta.sacar(self.valor_parcela)
                self.parcelas_restantes -= 1
                print(f"paga a parcela{self.parcelas-self.parcelas_restantes}, faltam {self.parcelas_restantes}")
            else:
                print("saldo insuficiente, parcela não paga!")
        else:
            print("emprestimo pago.")