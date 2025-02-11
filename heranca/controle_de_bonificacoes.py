from funcionario import Funcionario
class ControleDeBonificacoes:
    def __init__(self, total = 0):
        self._total = total

    def registra(self, funcionario):
        self._total += funcionario.get_bonificacao()

    def get_total(self):
        return self._total