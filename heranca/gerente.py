from funcionario import Funcionario
class Gerente(Funcionario): #funcionario é a superclasse de gerente
    def __init__(self, nome, salario, cpf, senha, qtde):
        super().__init__(nome, salario, cpf)
        self._senha = senha
        self._qtde = qtde

    def get_bonificacao(self):
        return self._salario * 0.2