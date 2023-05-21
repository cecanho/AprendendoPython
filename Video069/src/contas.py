from collections.abc import MutableSequence
from conta import Conta

class Contas(MutableSequence):
    _dados = []

    def __delitem__(self, posicao):
        del self._dados[posicao]

    def __getitem__(self, posicao):
        return self._dados[posicao]

    def __len__(self):
        return len(self._dados)

    def __setitem__(self, posicao, valor):
        if (isinstance(valor, Conta)):
            self._dados[posicao] = valor
        else:
            raise TypeError(f"Valor atribuído não é uma conta!")

    def insert(self, posicao, valor):
        if (isinstance(valor, Conta)):
            return self._dados.insert(posicao, valor)
        else:
            raise TypeError(f"Valor inserido não é uma conta!")