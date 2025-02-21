class Calculadora:
    def soma(self, *args):
        if type(args[0]) == str:
            soma = ''
            for i in args:
                soma+=i
            return soma
        else:
            soma = 0
            for i in args:
                soma += i
            return soma