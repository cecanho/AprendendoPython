from conta import Conta

class AtualizadorDeContas:
    def __init__(self, selic, saldo_total=0.0):
        self._selic = selic
        self._saldo_total = saldo_total

    @property
    def selic(self):
        return self._selic

    @selic.setter
    def selic(self, selic):
        self._selic = selic

    @property
    def saldo_total(self):
        return self._saldo_total

    @saldo_total.setter
    def saldo_total(self, saldo_total):
        self._saldo_total = saldo_total

    def roda(self, conta):
        print(f"Saldo da Conta: {conta.saldo}")
        self._saldo_total += conta.atualiza(self._selic)
        print(f"Saldo Final: {self._saldo_total}")