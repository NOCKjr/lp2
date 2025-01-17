from conta import Conta
from cliente import Cliente

cliente1 = Cliente("elias", "06064218231")
cliente2 = Cliente("sla", "34384783143")

c1 = Conta(1, cliente1, 1000, 11000)
c2 = Conta(2, cliente2, 0, 12321)

print(c1.saldo)
print(c2.saldo)

c1.transferir(c2, 400)

print(c1.saldo)
print(c2.saldo)

print(c1)