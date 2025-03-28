from abc import ABC, abstractmethod
class Conta(ABC):
    def __init__(self, n, cli, sal):
        self._numero = n
        self._titular = cli
        self._saldo = sal

    def atualiza(self, taxa):
        pass