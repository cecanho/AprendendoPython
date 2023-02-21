# Autor: Cristiano José Cecanho
# Aprendendo Python: Vídeo 043
# Data: 19-02-2023
# Objetivo: OO em Python - Slots - Classe Caneta
# Alterações baseadas na pág. 121-122 (128-129)

class Caneta:

    __slots__ = ['_marca', '_cor', '_ponta']

    def __init__(self, marca, cor, ponta):
        self._marca = marca
        self._cor = cor
        self._ponta = ponta

    def imprimir(self):
        print(f"\nMARCA: {self._marca}\n"
              f"COR: {self._cor}\n"
              f"ESP. PONTA: {self._ponta}\n")