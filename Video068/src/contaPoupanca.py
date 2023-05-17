from conta import Conta

class CP(Conta):
    def __init__(self, numero, tipo, titular, saldo, limite=0.0):
        super().__init__(numero, tipo, titular, saldo)

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3.0
        return self._saldo