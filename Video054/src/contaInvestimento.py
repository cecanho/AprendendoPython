from conta import Conta

class ContaInvestimento(Conta):
    def __init__(self, numero, tipo, titular, saldo, limite=0.0):
        super().__init__(numero, tipo, titular, saldo)

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5.0