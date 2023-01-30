# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 037
# Data: 29-01-2023
# Objetivo: OO em Python - Composição

import datetime

class Historico:

    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f"Data Abertura: {self.data_abertura}")
        print(f"Transações:")
        for t in self.transacoes:
            print(f" - {t}")