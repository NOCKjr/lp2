class Funcionario:
    def __init__(self, nome, salario, cpf):
        try:
            if(salario<0):
                raise ValueError
            self._nome = nome
            self._salario = salario
            self._cpf = cpf
        except ValueError:
            print("Salario não pode ser negativo!")

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if(valor<0):
            self._salario = valor

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cargo(self, cpf):
        self._cpf = cpf

    def get_bonificacao(self):
        return self._salario * 0.1

    def __str__(self):
        return f'Nome: {self._nome}, Salario: {self._salario}'