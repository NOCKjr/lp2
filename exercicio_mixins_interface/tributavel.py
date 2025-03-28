import abc
class TributavelInterface(abc.ABC):
    '''Essa é uma interface para tributaveis, logo é uma classe não instanciavel'''
    @abc.abstractmethod
    def valor_imposto(self):
        '''esse é um metodo abstrato, apenas obrigando as subclasses a instanciarem ele, logo não é implementavel'''
        pass