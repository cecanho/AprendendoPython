# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 033
# Data: 14-01-2023
# Objetivo: OO em Python

class Conta:
# Construtor da classe
    def __init__(self, titular, numero, saldo, limite):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if (self.limite + self.saldo >= valor):
            self.saldo -= valor
        else:
            print(f"Saldo insuficiente para saque: {self.limite + self.saldo}")

    def extrato(self):
        frase = f"{self.titular}\n" \
                f"Num.: {self.numero}\n" \
                f"Saldo (a): {self.saldo}\n" \
                f"Limite (b): {self.limite}\n" \
                f"Saldo Total (a+b): {self.limite + self.saldo}"
        return frase

    def setTitular(self, titular):
        self.titular = titular

    def setLimite(self, limite):
        self.limite = limite

