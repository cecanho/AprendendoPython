from Contas import Contas
from collections.abc import MutableMapping

class ListaContas(MutableMapping):
    _dados = []

    def __setitem__(self, posicao, valor):
       self._dados[posicao].valor = valor

    def __delitem__(self, posicao):
        del self._dados[posicao]

    def __getitem__(self, posicao):
        return self._dados[posicao]

    def __len__(self):
        return len(self._dados)

    def __iter__(self):
        return self._dados.__iter__()

    def insert(self, valor):
        if (isinstance(valor, Contas)):
            return self._dados.append(valor)
        else:
            raise TypeError(f"Valor inserido não é uma conta!")