from math import sqrt

from forma import Forma
class Triangulo(Forma):
    def __init__(self, a, b, c):
        try:
            super().__init__(a, b, c)
            self._a = a
            self._b = b
            self._c = c
        except ValueError as e:
            print(e)

    def perimetro(self):
        if self._tipo == 'Triangulo':
            return self._a + self._b + self._c
        else:
            return 0
    def area(self):
        if self._tipo == 'Triangulo':
            s = self.perimetro()/2
            return sqrt(s*(s-self._a)*(s-self._b)*(s-self._c))
