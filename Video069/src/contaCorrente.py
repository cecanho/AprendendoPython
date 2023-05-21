from conta import Conta
from TributavelMixIn import TributavelMixIn
from excecoes import SaldoInsuficienteError

class CC(Conta, TributavelMixIn):

    def __init__(self, numero, tipo, titular, saldo, limite=0.0):
        super().__init__(numero, tipo, titular, saldo)

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2.0
        return self._saldo

    def deposita(self, valor):
        if (valor < 0):
            raise ValueError('Você tentou depositar um valor negativo.')
        else:
            self._saldo += valor - 0.10

    def get_valor_imposto(self):
        return self._saldo * 0.01

if __name__ == '__main__':
    cc = CC('123-4', 'João', 1000.0, 1000.0)
    valor = -1000.0
    # valor = 5000.9
    try:
        # cc.saca(valor)
        # print(f"Saque de {valor} realizado com sucesso")
        cc.deposita(valor)
        print(f"Deposito de {valor} realizdo com sucesso")
    except ValueError:
        # print('O valor a ser sacado deve ser um número positivo.')
        print(f"O valor a ser depositado deve ser positivo")
    except SaldoInsuficienteError:
        print('Você não possui saldo suficiente para concluir esta operação.')