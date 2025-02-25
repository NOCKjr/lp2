from forma import Forma
class Quadrilatero(Forma):
    def __init__(self, lado1, lado2):
        super().__init__(lado1, lado2)
        self._lado1 = lado1
        self._lado2 = lado2
    def area(self):
        return self._lado1 * self._lado2
    def perimetro(self):
        return 2 * self._lado1 + 2 * self._lado2