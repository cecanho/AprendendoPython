# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 038
# Data: 29-01-2023
# Objetivo: OO em Python - Exercícios OO pag 107/114
import datetime

from data_abertura import Data_Abertura
from historico import Historico

class Conta:
    def __init__(self, numero, Cliente, saldo, limite):
        self.numero = numero
        self.titular = Cliente
        self.saldo = saldo
        self.limite = limite
        data = Data_Abertura()
        self.data_abertura = data.abertura_de_conta()
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f"Deposito de {valor}")

    def saca(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append(f"Saque de {valor}")
            return True

    def transfere(self, destino, valor):
        retirou = self.saca(valor)

        if(retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append(f"Transferência de {valor} para {destino.numero}")
            return True

    def extrato(self):
        print(f"Número: {self.numero}"
              f"\nSaldo: {self.saldo}"
              f"\nCliente: {self.titular.nome + ' ' + self.titular.sobrenome}"
              f"\nCPF: {self.titular.cpf}"
              f"\nConta aberta em: {self.data_abertura}")
        self.historico.transacoes.append(f"Extrato realizado em {datetime.date.today()}")