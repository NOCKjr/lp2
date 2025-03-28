from conta_corrente import ContaCorrente
from seguro import SeguroDeVida
from manipulador import ManipuladorDeTributaveis
cc1 = ContaCorrente(1, 'elias', 1000)
cc2 = ContaCorrente(2, 'elias2', 5000)
cc3 = ContaCorrente(3, 'elias3', 10000)

s1 = SeguroDeVida(1, 1500, 'elias')
s2 = SeguroDeVida(2, 3000, 'elias2')

lista_t = [cc1, cc2, cc3, s1, s2]
m1 = ManipuladorDeTributaveis()
m1.calcular_impostos(lista_t)
