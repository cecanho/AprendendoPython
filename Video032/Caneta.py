# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 032
# Data: 08-01-2023
# Objetivo: Classe Caneta

class Caneta:
    def __init__(self, marca, cor, ponta):
        self.marca = marca
        self.cor = cor
        self.ponta = ponta

    def escrever(self):
        print(f"A caneta {self.marca} de cor {self.cor} "
              f"tem espessura {self.ponta}")