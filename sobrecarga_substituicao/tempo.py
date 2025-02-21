class Tempo:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self._h = hora
        self._m = minuto
        self._s = segundo

    def __str__(self):
        return f'{self._h}:{self._m}:{self._s}'
