class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        if (self._saldo - valor < 0):
            print(f"SALDO INSUFICIENTE PARA ESTA OPERAÇÃO\n"
                  f"SALDO_ATUAL: {self._saldo}")
            return False
        else:
            self._saldo -= valor

    def extrato(self):
        print(f"\n{str.upper(self._titular)} - {self._numero}\n"
              f"SALDO: {self._saldo}\n"
              f"LIMITE: {self._limite}")

    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True

if __name__ == '__main__':
    conta = Conta('123-4', 'João', 1200.0, 1000.0)
    conta.deposita(100)
    conta.saca(150)
    conta2 = Conta('124-4', 'José', 1200.0, 1000.0)
    #conta.transfere_para(conta2, 1300.0)
    conta.transfere_para(conta2, 300)
    conta.extrato()
    conta2.extrato()