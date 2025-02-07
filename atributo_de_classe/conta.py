class Conta:
    _total_contas = 0 #atributo de classe
    __slots__ = ['_numero','_cliente' ,'_titular', '_saldo', '_limite']
    def __init__(self, numero, cliente, saldo, limite):
        self._numero = numero
        self._cliente = cliente
        self._saldo = saldo
        self._limite = limite
        Conta._total_contas += 1


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

    @staticmethod
    def total_contas():
        return Conta._total_contas

    @classmethod
    def total_contas_classe(cls):
        return cls._total_contas