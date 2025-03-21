from abc import ABC, abstractmethod
class Funcionario(ABC):
    @abstractmethod
    def bonificacao(self):
        pass