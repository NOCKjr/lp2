from circulo import Circulo
from quadrilatero import Quadrilatero
from triangulo import Triangulo
c1 = Circulo(10)
q1 = Quadrilatero(4, 5)
t1 = Triangulo(1, 2,3)
formas = [c1, q1, t1]
for i in formas:
    print(i)