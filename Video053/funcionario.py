import abc

class Funcionario(abc.ABC):
    def __init__(self, nome, cpf, salario, agencia, limite):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._agencia = agencia
        self._limite = limite

    @abc.abstractmethod
    def get_bonificacao(self):
        pass
