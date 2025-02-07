from conta import Conta
c1 = Conta(101, 'fulano', 1000,200)
print(c1.total_contas()) #metodo estático
print(Conta.total_contas()) #metodo estático
print(Conta.total_contas_classe()) #metodo de classe

c1.chave_pix = '6989348349348' #não será possivel pelo slots em conta