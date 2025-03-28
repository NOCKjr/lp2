from conta import Conta
from tributavel import TributavelInterface
class ContaCorrente(Conta, TributavelInterface):
    def atualiza(self, taxa):
        valor = self._saldo * taxa * 2
        self.depositar(valor)
        self.sacar(0.1)
        return valor

    def valor_imposto(self):
        return self._saldo * 0.02