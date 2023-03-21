from conta import Conta

class CP(Conta):

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
        return self._saldo