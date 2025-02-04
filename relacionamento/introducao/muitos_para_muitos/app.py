from cliente import Cliente
from conta import Conta
cliente1 = Cliente("fulano", '123')
cliente2 = Cliente("beltrano", '456')
conta1 = Conta(101, 0, 0)
conta2 = Conta(102, 100, 100)

cliente1.adicionar_conta(conta1, 'titular')
cliente1.adicionar_conta(conta2, 'titular')

cliente1.listar_contas()