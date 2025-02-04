class Funcionario:
    def __init__(self, nome, salario, cargo):
        try:
            if(salario<0):
                raise ValueError
            self._nome = nome
            self._salario = salario
            self._cargo = cargo
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
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo
    def trocar_cargo(self, novo_cargo):
        self.cargo = novo_cargo
        print("Cargo trocado com sucesso!")
    def aumentar_salario(self, percentual):
        try:
            if(percentual<0):
                raise ValueError
            self.salario += percentual * self.salario
            print(f'Novo salario: {self.salario}')
        except ValueError:
            print("Percentual não pode ser negativo")