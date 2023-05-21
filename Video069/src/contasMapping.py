from collections.abc import MutableMapping

from conta import Conta

class ContaMapping(MutableMapping):
    _dados = []

    def __setitem__(self, posicao, valor):
        if (isinstance(valor, Conta)):
            self._dados[posicao] = valor
        else:
            raise TypeError(f"Valor atribuído não é uma conta!")

    def __delitem__(self, posicao):
        del self._dados[posicao]

    def __getitem__(self, posicao):
        return self._dados[posicao]

    def __len__(self):
        return len(self._dados)

    def __iter__(self):
        return self._dados.__iter__()

    def insert(self, valor):
        if (isinstance(valor, Conta)):
            return self._dados.append(valor)
        else:
            raise TypeError(f"Valor inserido não é uma conta!")
