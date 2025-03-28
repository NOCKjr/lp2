from tributavel import TributavelInterface
class ManipuladorDeTributaveis:
    def calcular_impostos(self, tributaveis: list):
        soma = 0
        for i in tributaveis:
            if isinstance(i, TributavelInterface):
                soma+=i.valor_imposto()
        print(f'O total de imposto desses tributaveis são de {soma}')