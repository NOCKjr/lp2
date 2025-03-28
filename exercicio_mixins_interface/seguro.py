from tributavel import TributavelInterface
class SeguroDeVida(TributavelInterface):
    def __init__(self, numero, valor_seguro, titular):
        self._numero = numero
        self._valor_seguro = valor_seguro
        self._titular = titular
    def valor_imposto(self):
        return 34+self._valor_seguro*0.05
