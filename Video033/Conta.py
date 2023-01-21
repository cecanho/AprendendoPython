# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 033-034-035
# Data: 21-01-2023
# Objetivo: OO em Python

class Conta:
# Construtor da classe
    def __init__(self, cliente, numero, saldo, limite=1000.0):
        self.titular = cliente
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if (self.limite + self.saldo >= valor):
            self.saldo -= valor
        else:
            print(f"Saldo insuficiente para saque/transferência: {self.limite + self.saldo}\n")
            return False

    def extrato(self):
        frase = f"{self.titular.nome}\n" \
                f"Num.: {self.numero}\n" \
                f"Saldo (a): {self.saldo}\n" \
                f"Limite (b): {self.limite}\n" \
                f"Saldo Total (a+b): {self.limite + self.saldo}"
        return frase

    def setTitular(self, titular):
        self.titular = titular

    def setLimite(self, limite):
        self.limite = limite

    def transfere(self, destino, valor):
        retirada = self.saca(valor)
        if (retirada == False):
            return False
        else:
            destino.deposita(valor)
            return True

