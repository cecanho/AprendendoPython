from collections.abc import MutableSequence
from funcionario import Funcionario

class Funcionarios(MutableSequence):
    _dados = []

    def __contains__(self, item):
        return self._dados.__contains__(self, item)

    def __len__(self):
        return len(self._dados)

    def __getitem__(self, posicao):
        return self._dados[posicao]

    def __setitem__(self, posicao, valor):
        if (isinstance(valor, Funcionario)):
            self._dados[posicao] = valor
        else:
            raise TypeError('Valor atribuído não é um Funcionário')

    def __delitem__(self, posicao):
        del self._dados[posicao]

    def insert(self, posicao, valor):
        if (isinstance(valor, Funcionario)):
            return self._dados.insert(posicao, valor)
        else:
            raise TypeError('Valor inserido não é um Funcionário')

'''if __name__ == '__main__':
    funcionarios = Funcionarios()
    print(funcionarios.__len__())
    print(funcionarios)'''