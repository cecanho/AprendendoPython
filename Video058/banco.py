from conta import Conta
from contaCorrente import CC
from contaPoupanca import CP

class Banco:
    def __init__(self):
        self._lista_contas = []
        self._totalDeContas = 0

    @property
    def totalDeContas(self):
        return self._totalDeContas

    def adiciona(self, conta):
        self._lista_contas.append(conta)
        self._totalDeContas += 1

    def pegaConta(self, numero):
        posicao = -1
        for c in self._lista_contas:
            if (numero == c.numero):
                c.extrato()
            posicao += 1
        print(f"Posição: {posicao}")