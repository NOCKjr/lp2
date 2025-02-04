class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self._numero = numero
        self._cliente = cliente
        self._saldo = saldo
        self._limite = limite


    #forma pythonica
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    #convenção padrão para getters e setters
    def get_saldo(self):
        return self._saldo
    #esse metodo não faz sentido
    def set_saldo(self, valor):
        self._saldo = valor