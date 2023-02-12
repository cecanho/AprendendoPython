# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 041
# Data: 12-02-2023
# Objetivo: OO em Python - Atributos de classe
# Alterações baseadas na pág. 120 (127)
import datetime

from data_abertura import Data_Abertura
from historico import Historico

class Conta:

    _total_contas = 0

    def get_total_contas(self):
        return Conta._total_contas

    def __init__(self, agencia, Cliente, saldo, limite):
        Conta._total_contas += 1
        self._numero = agencia + '-' + str(self.get_total_contas())
        self._titular = Cliente
        self._saldo = saldo
        self._limite = limite
        data = Data_Abertura()
        self._data_abertura = data.abertura_de_conta()
        self._historico = Historico()

    def deposita(self, valor):
        self._saldo += valor
        self._historico.transacoes.append(f"Deposito de {valor}")

    def saca(self, valor):
        if(self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            self._historico.transacoes.append(f"Saque de {valor}")
            return True

    def transfere(self, destino, valor):
        retirou = self.saca(valor)

        if(retirou == False):
            return False
        else:
            destino.deposita(valor)
            self._historico.transacoes.append(f"Transferência de {valor} para {destino._numero}")
            return True

    def extrato(self):
        print(f"Número: {self._numero}"
              f"\nSaldo: {self._saldo}"
              f"\nCliente: {self._titular.nome + ' ' + self._titular.sobrenome}"
              f"\nCPF: {self._titular.cpf}"
              f"\nConta aberta em: {self._data_abertura}"
              f"\nTotal contas: {self.get_total_contas()}")
        self._historico.transacoes.append(f"Extrato realizado em {datetime.date.today()}")