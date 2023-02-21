# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 044
# Data: 21-02-2023
# Objetivo: OO em Python - Exercícios da pág. 123-125 (130-133)

class Conta:

    #__slots__ = ['_numero', '_titular', '_saldo', '_limite']

    identificador = 1

    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self.identificador = Conta.identificador
        Conta.identificador += 1

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if(saldo < 0):
            print('Saldo não pode ser negativo')
        else:
            self._saldo = saldo

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
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite