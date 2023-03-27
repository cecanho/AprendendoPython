from conta import Conta

class CC(Conta):

    def __init__(self, numero, tipo, titular, saldo, limite=0.0):
        super().__init__(numero, tipo, titular, saldo)

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2.0
        return self._saldo

    def deposita(self, valor):
        self._saldo += valor - 0.10