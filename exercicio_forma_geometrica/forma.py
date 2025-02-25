class Forma:
    def __init__(self, *args):
        self._tam = len(args)
        if self._tam == 1:
            self._tipo = 'Circulo'
        elif self._tam == 2:
            self._tipo = 'Retangulo'
            if args[0] == args[1]:
                self._tipo = 'Quadrado'
        elif self._tam == 3:
            self._a = args[0]
            self._b = args[1]
            self._c = args[2]
            if self._a < (self._c+self._b) and self._b < (self._c+self._a) and self._c < (self._a+self._b):
                self._tipo = 'Triangulo'
            else:
                self._tipo = 'Forma desconhecida'
                raise ValueError('Quantidade de parametros invalida.')
        else:
            self._tipo = 'Forma desconhecida'

    def area(self):
        pass

    def perimetro(self):
        pass

    def __str__(self):
        if self._tipo != 'Forma desconhecida':
            return f'{self._tipo} Area: {self.area()} Perimetro: {self.perimetro()}'
        else:
            return f'{self._tipo} não tem area e perimetro.'