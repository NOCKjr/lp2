from sobrecarga import Sobrecarga
from sobrecarga import Sobrecarga2
from calculadora import Calculadora
from data import Data
from datetime import date
from tempo import Tempo
from pessoa import Pessoa
s1 = Sobrecarga()
s2 = Sobrecarga2()
s3 = Sobrecarga2(1)
s4 = Sobrecarga2(1, 2)
s5 = Sobrecarga2(1, 2, 3)

#calculadora
c1 = Calculadora()
print(c1.soma(1, 2, 3, 4, 5))
print(c1.soma('a', 'b'))

#data
d1 = Data('2025-02-20')
d2 = Data(date.today())
print(d1)
print(d2)

# tempo
t1 = Tempo(8, 10, 30)
print(t1)

# pessoa
p1 = Pessoa('fulano', 12)
p2 = Pessoa.criar_pessoa()
print(p1)
print(p2)