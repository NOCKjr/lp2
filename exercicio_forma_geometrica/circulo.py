import math
from forma import Forma
class Circulo(Forma):
    def __init__(self, raio):
        super().__init__(raio)
        self._raio = raio

    def area(self):
        return math.pi * self._raio**2
    def perimetro(self):
        return 2 * math.pi * self._raio
