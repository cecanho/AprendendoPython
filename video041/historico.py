import datetime


class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print(f"Data de abertura da conta: {self.data_abertura}"
              f"\nTransações:")
        for t in self.transacoes:
            print("-", t)