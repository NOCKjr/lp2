class Sobrecarga:
    def __init__(self):
        print('1')
    def __init__(self):
        print('2')
    def __init__(self):
        print('3')

class Sobrecarga2:
    def __init__(self, *args):
        self._tam = len(args)
        self.__str__()

    def __str__(self):
        if self._tam == 0:
            print('zero')
        elif self._tam == 1:
            print('um')
        elif self._tam == 2:
            print('dois')
        else:
            print('mais que dois')