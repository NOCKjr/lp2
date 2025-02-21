class Pessoa:
    def __init__(self, nome, idade=None):
        self._nome = nome
        self._idade = idade

    @classmethod
    def criar_pessoa(cls):
        return cls('Anonimo')

    def __str__(self):
        return f'nome: {self._nome} idade: {self._idade}'