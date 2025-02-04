from hotel import Hotel
from quarto import Quarto
from cliente import Cliente
hotel = Hotel('Uirapuru', "rua uirapuru")

c1 = Cliente("elias", 6064218231)

q1 = Quarto(101, 2)
q2 = Quarto(102, 3)
q3 = Quarto(103, 1)

hotel.incluir_quarto(q1)
hotel.incluir_quarto(q2)
hotel.incluir_quarto(q3)
hotel.verificar_disponibilidade()
hotel.reservar_quarto(101, c1)

hotel.verificar_disponibilidade()

hotel.liberar_quarto(101)

hotel.verificar_disponibilidade()